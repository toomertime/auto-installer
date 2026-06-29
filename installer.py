import subprocess

def install_app(winget_id):
    subprocess.run(["winget", "install", winget_id])