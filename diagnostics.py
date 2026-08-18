# v2.1.0

import shutil
import subprocess
from dataclasses import dataclass
from enum import Enum

# Machine-readable status codes for WinGet environment
# that can be passed to GUI.
class DiagnosticStatus(Enum):
    WINGET_OK = "winget_ok"
    WINGET_NOT_FOUND = "winget_not_found"
    WINGET_CANNOT_EXECUTE = "winget_cannot_execute"
    WINGET_SOURCE_MISSING = "winget_source_missing"
    WINGET_TIMEOUT = "winget_timeout"
    WINGET_ERROR = "winget_error"


# Represents the results of the WinGet environtment check.
# GUI can use this info to decide whether installations
# should be allowed to start.
@dataclass
class DiagnosticResult:
    ready: bool
    status: DiagnosticStatus
    winget_path: str | None
    winget_version: str | None
    winget_source_available: bool
    error: str | None = None


def check_winget():
    """
    Check whether WinGet is available and usable.
    
    Checks include:
    - Can Windows locate winget?
    - Can Windows execute winget?
    - Is the WinGet package source available?
    """

    # Find the executable that Windows would use when "winget" is run 
    # from this Python process.
    winget_path = shutil.which("winget")
    winget_version = None

    if winget_path is None:
        return DiagnosticResult(
            ready=False,
            status=DiagnosticStatus.WINGET_NOT_FOUND,
            winget_path=None,
            winget_version=None,
            winget_source_available=False,
            error="WinGet could not be found."
        )
    
    try:
        # Verify WinGet can start.
        # Seperate from shutil.which() because Windows may find
        # winget.exe but fail when attempting to run.
        version_result = subprocess.run(
            [winget_path, "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if version_result.returncode != 0:
            return DiagnosticResult(
                ready=False,
                status=DiagnosticStatus.WINGET_ERROR,
                winget_path=winget_path,
                winget_version=None,
                winget_source_available=False,
                error="WinGet started but returned error when checking version."
            )
        
        winget_version = version_result.stdout.strip()

        # Check which package sources are currently registered.
        source_result = subprocess.run(
            [winget_path, "source", "list"],
            capture_output=True,
            text=True,
            timeout=15
        )

        if source_result.returncode != 0:
            return DiagnosticResult(
                ready=False,
                status=DiagnosticStatus.WINGET_ERROR,
                winget_path=winget_path,
                winget_version=winget_version,
                winget_source_available=False,
                error="WinGet could not read its package sources."
            )


        # Look for the standard source named exactly "winget".
        winget_source_available = any(
            line.split()[0] == "winget"
            for line in source_result.stdout.splitlines()
            if line.split()
        )

        if not winget_source_available:
            return DiagnosticResult(
                ready=False,
                status=DiagnosticStatus.WINGET_SOURCE_MISSING,
                winget_path=winget_path,
                winget_version=winget_version,
                winget_source_available=False,
                error="The WinGet package source is not available."
            )
        
        # All required checks passed.
        return DiagnosticResult(
            ready=True,
            status=DiagnosticStatus.WINGET_OK,
            winget_path=winget_path,
            winget_version=winget_version,
            winget_source_available=True
        )
    
    except FileNotFoundError:
        # The executable disapeared or became inaccessible
        # between path check and launch attempt.
        return DiagnosticResult(
            ready=False,
            status=DiagnosticStatus.WINGET_CANNOT_EXECUTE,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error="WinGet could not be found when Windows tried to start it."
        )
    
    except subprocess.TimeoutExpired:
        # WinGet exists, but doesn't respond in a reasonable amount of time.
        return DiagnosticResult(
            ready=False,
            status=DiagnosticStatus.WINGET_TIMEOUT,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error="WinGet did not respond."
        )
    
    except OSError as exc:
        # Windows located WinGet but could not launch it.
        return DiagnosticResult(
            ready=False,
            status=DiagnosticStatus.WINGET_CANNOT_EXECUTE,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error=f"Windows could not start WinGet: {exc}"
        )
    
    except Exception as exc:
        # Prevent unexpected diagnostic failure from crashing
        # entire application.
        return DiagnosticResult(
            ready=False,
            status=DiagnosticStatus.WINGET_ERROR,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error=f"An unexpected diagnostic error has occurred: {exc}"
        )