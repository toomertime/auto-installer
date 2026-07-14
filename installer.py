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
    
    if "process_name" in app:
        subprocess.run(["taskkill", "/f", "/im", app["process_name"]])