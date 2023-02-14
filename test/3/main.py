import customtkinter as tk
from video import videoPlayer
# from MyCustomTkinter import MyCustomTkinter as mtk

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

# LabelFrame = mtk.LabelFrame(root,text="Get video by URL",width=200,height=100)
# urlEntry = tk.CTkEntry(LabelFrame,width=200)
# urlEntry.grid(row=0,column=0)
# LabelFrame.pack(pady=10,padx=10)
# urlEntry.pack()



root.mainloop()