import customtkinter as tk
import sub
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

res = "500x500"
window_name = "ex"
root = tk.CTk()
root.geometry(res)
root.title(window_name)


frame = tk.CTkFrame(root)
label = tk.CTkLabel(frame,text="Hello world")
button = tk.CTkButton(frame,text="nyanmo")
button.bind("<1>",lambda self:sub.scrolledtext(root))
label.pack()
button.pack()
frame.pack(pady=20,ipadx=20,ipady=20)

root.mainloop()