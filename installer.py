# v2.1.0

import subprocess
from dataclasses import dataclass

# Represents the final result of an attmepted application install.
# This allows the GUI to know whether the install succeeded,
# what WinGet returned, and what error occured if it failed.
@dataclass
class InstallResult:
    app_name: str
    success: bool
    return_code: int | None
    output: str
    error: str | None = None

def build_install_command(app):
    """
    Build the WinGet command for a single application.
    App-specific options such as install location or override arguments
    are added only when they exist in the catalog entry.
    """

    cmd = [
        "winget",
        "install",
        "--id", app["winget_id"],
        "--exact",
        "--silent",
        "--disable-interactivity", 
        "--accept-package-agreements",
        "--accept-source-agreements", 
    ]

    # Some apps may need to be installed to a specific directory.
    if "install_location" in app:
        cmd += ["--location", app["install_location"]]


    # Some instllers require custom arguments instead of WinGet's defaults.
    if "override" in app:
        cmd += ["--override", app["override"]]

    return cmd

def cleanup_processes(app):
    """
    Close any processes that an installer automatically launches.
    """
    for process_name in app.get("cleanup_processes", []):
        subprocess.run(
            ["taskkill", "/f", "/t", "/im", process_name],
            capture_output=True,
            text=True
        )

def install_app(app):
    """
    Install one app using WinGet.

    WinGet out put is captured while being printed to the console and 
    the Winget process reuturn code determines whether the install succeeded.
    """

    app_name = app["name"]
    cmd = build_install_command(app)

    # Store WinGet output
    output_lines = []

    try:
        # Start WinGet as a child process.
        # stderr is redirected into stdout so all WinGet messages
        # can be cptured through a single stream.
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        # Read WinGet output as it happens.
        if process.stdout is not None:
            for line in process.stdout:
                print(line, end="")
                output_lines.append(line)

        # Wait for WinGet to completely finish and get exit code.
        return_code = process.wait()

        # Convert collected output lines into one string.
        output = ''.join(output_lines)

        # Return code 0 indicates success.
        if return_code == 0:
            # Some apps automatically launch after installation.
            # Close those processes only after WinGet has fully completed.
            cleanup_processes(app)

            return InstallResult(
                app_name=app_name,
                success=True,
                return_code=return_code,
                output=output
            )
        
        # WinGet launched successfully, but installation failed.
        return InstallResult(
            app_name=app_name,
            success=False,
            return_code=return_code,
            output=output,
            error=f"WinGet exited with code {return_code}"
        )
    
    except FileNotFoundError:
        # Python could not locate the winget executable.
        return InstallResult(
            app_name=app_name,
            success=False,
            return_code=None,
            output="",
            error="WinGet could not be found."
        )
    
    except OSError as exc:
        # Windows found excutable but could not start it.
        return InstallResult(
            app_name=app_name,
            success=False,
            return_code=None,
            output="",
            error=f"Windows could not start WinGet: {exc}"
        )
    
    except Exception as exc:
        # Catch any unexpected failure so one app cannot crash
        # the entire batch install process.
        return InstallResult(
            app_name=app_name,
            success=False,
            return_code=None,
            output="",
            error=f"Unexpected error:: {exc}"
        )

