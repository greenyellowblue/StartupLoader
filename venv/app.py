import tkinter as tk
from tkinter import filedialog, Text
import os
import sys, subprocess
rootWin = tk.Tk()

# initialize saved apps to execute as array
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# Button call functions
def addApp():  # Adds an app to saved applications

    # Clear all current saved in apps array so we do not print out same apps more than once
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Application", "*.app"), ("all files", "*./")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg = "seashell")
        label.pack()


def open_file(filename):  # open_file function to help open files on non-windows systems
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def runApps():  # Run all apps in saved applications
    for app in apps:
        open_file(app)


# Draw all GUI
canvas = tk.Canvas(rootWin, height=800, width=800, bg="light sea green")
canvas.pack()

frame = tk.Frame(rootWin, bg="seashell")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(rootWin, text="Add Program", padx=10, pady=5, fg="white", bg="#263D42", command= addApp)
runApps = tk.Button(rootWin, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command = runApps)


openFile.pack()
runApps.pack()

for app in apps:
    label = tk.Label(frame, text = app, bg = "seashell")
    label.pack()

rootWin.mainloop()


with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

