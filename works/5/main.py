import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
res = "500x500"
window_name = "Paint"

def _resizeEnevtHandler(root:tk.CTk,canvas:tk.CTkCanvas):
    canvas.configure(width=root.winfo_width(),height=root.winfo_height())

root = tk.CTk()
root.geometry(res)
root.title(window_name)

canvas = tk.CTkCanvas(root,width=root.winfo_width(),height=root.winfo_height(),bg="gray")
canvas.pack(padx=10,pady=10)
root.bind("<Configure>",lambda tets:_resizeEnevtHandler(root,canvas))

root.mainloop()