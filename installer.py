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
            print(f"Killing process: {proc.name()} (PID: {pid})")
            proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def install_app(app):
    pids_before = get_pids()

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

    if not app.get("skip_cleanup"):
        kill_new_processes(pids_before)