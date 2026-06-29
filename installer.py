import subprocess

def install_app(app):
    # Run the winget install command for the given winget ID
    subprocess.run([
        "winget", "install",
        "--silent", 
        "--accept-package-agreements",
        "--accept-source-agreements", 
        app["winget_id"]
    ])
    # iff app has a process_name, attempt to kill it after installation
    if "process_name" in app:
        subprocess.run(["taskkill", "/f", "/im", app["process_name"]])
    