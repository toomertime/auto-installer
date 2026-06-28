import subprocess

def install_app(winget_id):
    # Run the winget install command for the given winget ID
    subprocess.run(["winget", "install", winget_id])