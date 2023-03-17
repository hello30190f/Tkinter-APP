
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
res = "500x500"
window_name = "ex"
root = tk.CTk()
root.geometry(res)
root.title(window_name)
root.mainloop()