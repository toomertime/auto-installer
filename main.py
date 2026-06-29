from pydoc import text
import tkinter as tk
import threading
from installer import install_app
from catalog import APPS

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Installer")
        self.root.geometry("400x300")

        # List of boolean variables for each app
        self.vars = []

        # Select all checkbox at the top
        self.select_all_var = tk.BooleanVar()
        select_all_chk = tk.Checkbutton(self.root, text="Select All", variable=self.select_all_var, anchor="w", command=self.toggle_all)
        select_all_chk.pack(fill="x")

        # Space between the select all checkbox and the app list
        tk.Label(self.root, text="").pack()

        # Create a checkbox for each app in the catalog
        for app in APPS:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.root, text=app["name"], variable=var, anchor="w")
            checkbox.pack(fill="x")
            self.vars.append(var)

        # Install button triggers installation process
        install_btn = tk.Button(self.root, text="Install", command=self.start_install)
        install_btn.pack()

        # Status label to display installation progress
        self.status_label = tk.Label(self.root, text="Ready")
        self.status_label.pack()

    def toggle_all(self):
        # Toggle all checkboxes to match the select all checkbox
        for var in self.vars:
            var.set(self.select_all_var.get())

    def update_status(self, text):
        # Update the status label with the given text in main thread
        self.root.after(0, lambda: self.status_label.config(text=text))
    
    def on_install(self):
        for app, var in zip(APPS, self.vars):
            # Loop through each app and install checked ones
            if var.get():
                self.status_label.config(f"Installing {app['name']}...")
                install_app(app["winget_id"])
        self.update_status("Installation complete")

    def start_install(self):
        # Run installation in a background thread to avoid freezing the UI
        install_thread = threading.Thread(target=self.on_install)
        install_thread.start()

root = tk.Tk()
app = App(root)
root.mainloop()

