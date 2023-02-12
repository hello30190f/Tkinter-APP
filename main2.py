import customtkinter as tk
import sub
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

res = "500x500"
window_name = "App menu"
root = tk.CTk()
# root.geometry(res)
root.title(window_name)

sub.menu(root)

root.mainloop()