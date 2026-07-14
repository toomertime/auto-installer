import subprocess

def install_app(app):
    if app.get("requires_non_admin"):
        winget_cmd = f'winget install --silent --accept-package-agreements --accept-source-agreements {app["winget_id"]}'
        subprocess.run(["runas", "/trustlevel:0x20000", f"cmd.exe /c {winget_cmd}"])
        return
    
    cmd = [
        "winget", "install",
        "--silent", 
        "--accept-package-agreements",
        "--accept-source-agreements", 
        app["winget_id"]
    ]
    if "install_location" in app:
        cmd += ["--location", app["install_location"]]

    subprocess.run(cmd)
    