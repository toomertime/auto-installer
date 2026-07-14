import subprocess
import psutil

def get_pids():
    return set(psutil.pids())

def kill_new_processes(pids_before):
    pids_after = get_pids()
    new_pids = pids_after - pids_before
    for pid in new_pids:
        try:
            proc = psutil.Process(pid)
            proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def install_app(app):
    pids_before = get_pids()

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
    kill_new_processes(pids_before)
    
    