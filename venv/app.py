import tkinter as tk
from tkinter import filedialog, Text
import os

rootWin = tk.Tk()

canvas = tk.Canvas(rootWin, height = 800, width = 800, bg="#263D42")
canvas.pack()

frame = tk.Frame(rootWin, bg="white")
frame.place(relwidth=0.8, relheight = 0.8, relx=0.1, rely= 0.1)


rootWin.mainloop()