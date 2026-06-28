import tkinter as tk
import threading
from installer import install_app
from catalog import APPS

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Installer")
        self.root.geometry("400x300")

        self.vars = []
        self.select_all_var = tk.BooleanVar()
        select_all_chk = tk.Checkbutton(self.root, text="Select All", variable=self.select_all_var, anchor="w", command=self.toggle_all)
        select_all_chk.pack(fill="x")
        tk.Label(self.root, text="").pack()

        for app in APPS:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.root, text=app["name"], variable=var, anchor="w")
            checkbox.pack(fill="x")
            self.vars.append(var)

        install_btn = tk.Button(self.root, text="Install", command=self.start_install)
        install_btn.pack()
        self.status_label = tk.Label(self.root, text="Ready")
        self.status_label.pack()

    def toggle_all(self):
        for var in self.vars:
            var.set(self.select_all_var.get())

    def on_install(self):
        for app, var in zip(APPS, self.vars):
            if var.get():
                self.status_label.config(text=f"Installing {app['name']}...")
                install_app(app["winget_id"])
        self.status_label.config(text="Installation complete")

    def start_install(self):
        install_thread = threading.Thread(target=self.on_install)
        install_thread.start()

root = tk.Tk()
app = App(root)
root.mainloop()

