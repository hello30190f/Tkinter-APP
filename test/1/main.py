import os
from tkinter import filedialog

def IO_OfFile():
    # files = filedialog.askopenfiles(mode="wt")
    files = filedialog.asksaveasfile(mode="wt")
    files.write("Hello naynmo")
    files.close()
    # for file in files:
    #     file.write("Hello world")
    #     file.close()

IO_OfFile()