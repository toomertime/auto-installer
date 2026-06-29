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
    print(cmd) #debug
    subprocess.run(cmd)
    
    # iff app has a process_name, attempt to kill it after installation
    if "process_name" in app:
        subprocess.run(["taskkill", "/f", "/im", app["process_name"]])
    