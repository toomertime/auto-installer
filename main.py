import tkinter as tk
from installer import install_app
from catalog import APPS

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Installer")
        self.root.geometry("400x300")

        self.vars = []

        for app in APPS:
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.root, text=app["name"], variable=var, anchor="w")
            checkbox.pack(fill="x")
            self.vars.append(var)

        install_btn = tk.Button(self.root, text="Install", command=self.on_install)
        install_btn.pack()

    def on_install(self):
        for app, var in zip(APPS, self.vars):
            if var.get():
                print(f"Installing {app['name']}...")
                install_app(app["winget_id"])

root = tk.Tk()
app = App(root)
root.mainloop()

