import tkinter as tk
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

        install_btn = tk.Button(self.root, text="Install")
        install_btn.pack()

root = tk.Tk()
app = App(root)
root.mainloop()

