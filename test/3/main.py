import customtkinter as tk
from video import videoPlayer

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

# def menu(root:tk.CTk):
    




videoIns = videoPlayer()


# res = "1000x1000"
window_name = "Video player with vlc"
root = tk.CTk()
# root.geometry(res)
root.title(window_name)

button = tk.CTkButton(root,text="Launch video player")
button.bind("<1>",lambda self:videoIns.MainPlayer(root))
button.pack(pady=10,padx=10)

root.mainloop()