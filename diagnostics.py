# v2.0.0

import shutil
import subprocess
from dataclasses import dataclass

@dataclass
class DiagnosticResults:
    ready: bool
    winget_path: str | None
    winget_version: str | None
    winget_source_available: bool
    error: str | None = None

def check_winget():
    winget_path = shutil.which("winget")

    if winget_path is None:
        return DiagnosticResults(
            ready=False,
            winget_path=None,
            winget_version=None,
            winget_source_available=False,
            error="WinGet could not be found."
        )
    
    try:
        version_result = subprocess.run(
            [winget_path, "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if version_result.returncode != 0:
            return DiagnosticResults(
                ready=False,
                winget_path=winget_path,
                winget_version=None,
                winget_source_available=False,
                error="WinGet started but returned error when checking version."
            )
        
        winget_version = version_result.stdout.strip()

        source_result = subprocess.run(
            [winget_path, "source", "list"],
            capture_output=True,
            text=True,
            timeout=15
        )

        if source_result.returncode != 0:
            return DiagnosticResults(
                ready=False,
                winget_path=winget_path,
                winget_version=winget_version,
                winget_source_available=False,
                error="WinGet could not read its package sources."
            )

        winget_source_available = any(
            line.split()[0] == "winget"
            for line in source_result.stdout.splitlines()
            if line.split()
        )

        if not winget_source_available:
            return DiagnosticResults(
                ready=False,
                winget_path=winget_path,
                winget_version=winget_version,
                winget_source_available=False,
                error="The WinGet package source is not available."
            )
        
        return DiagnosticResults(
            ready=True,
            winget_path=winget_path,
            winget_version=winget_version,
            winget_source_available=True
        )
    
    except FileNotFoundError:
        return DiagnosticResults(
            ready=False,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error="WinGet could not be found when windows tried to start it."
        )
    
    except subprocess.TimeoutExpired:
        return DiagnosticResults(
            ready=False,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error="WinGet did not respond."
        )
    
    except OSError as exc:
        return DiagnosticResults(
            ready=False,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error=f"Windows could not start WinGet: {exc}"
        )
    
    except Exception as exc:
        return DiagnosticResults(
            ready=False,
            winget_path=winget_path,
            winget_version=None,
            winget_source_available=False,
            error=f"An unexpected diagnostic error has occurred: {exc}"
        )