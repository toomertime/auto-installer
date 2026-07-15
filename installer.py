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
    
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    for line in process.stdout:
        print(line, end="")
        if "Successfully installed" in line:
            if "cleanup_processes" in app:
                for p in app["cleanup_processes"]:
                    subprocess.run(["taskkill", "/f", "/t", "/im", p], capture_output=True)
    
    process.wait()

