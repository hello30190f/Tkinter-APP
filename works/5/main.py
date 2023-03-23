import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
from canvas import boxAndPhysics

res = "500x500"
window_name = "Paint"

root = tk.CTk()
canvasIns = boxAndPhysics(root)
root.geometry(res)
root.title(window_name)


root.mainloop()