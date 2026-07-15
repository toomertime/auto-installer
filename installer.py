import subprocess
import time
import threading

def kill_process_when_found(processes, stop_event):
    while not stop_event.is_set():
        for process in processes:
            subprocess.run(["taskkill", "/f", "/im", process], capture_output=True)
        time.sleep(1)

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
    
    if "cleanup_processes" in app:
        stop_event = threading.Event()
        cleanup_thread = threading.Thread(
            target=kill_process_when_found,
            args=(app["cleanup_processes"], stop_event)
        )
        cleanup_thread.daemon = True
        cleanup_thread.start()

    subprocess.run(cmd)
    
    if "cleanup_processes" in app:
        stop_event.set()
        cleanup_thread.join()
