import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []





def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executable", "*exe"), ("all files", "*.*")))
    if filename != "":
        apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="#20B7EE")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#20B7EE")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApp = f.read()
        tempApp = tempApp.split(',')
    for app in tempApp:
        if app != "":
            label = tk.Label(frame, text=app, bg="#20B7EE")
            label.pack()

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="black", bg="#20B7EE", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="black", bg="#20B7EE", command=runApps)
runApps.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

