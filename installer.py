import subprocess

def install_app(app):
    cmd = [
        "winget", "install",
        "--silent", 
        "--accept-package-agreements",
        "--accept-source-agreements", 
        app["winget_id"]
    ]
    if "install_location" in app:
        cmd += ["--location", app["install_location"]]
    if "override" in app:
        cmd += ["--override", app["override"]]

    subprocess.run(cmd)
    
    if "cleanup_processes" in app:
        for process in app["cleanup_processes"]:
            subprocess.run(["taskkill", "/f", "/im", process], capture_output=True)
