from tkinter import filedialog
import vlc
import customtkinter as tk

def videoPlayWay():
    vlcIns = vlc.MediaPlayer(filedialog.askopenfilename())
    while True:
        vlcIns.play()

# https://stackoverflow.com/questions/47990695/how-to-embed-a-vlc-instance-in-a-tkinter-frame

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

# def video(display:tk.CTkFrame):

    # pass

# import tkinter as tk
res = "800x700"
window_name = "sample video player"
root = tk.CTk()
root.geometry(res)
root.title(window_name)

Main = tk.CTkFrame(root,width=700,height=700)
Main.grid(row=0,column=0)

displayP = tk.CTkFrame(Main)
displayP.place(relwidth=1,relheight=1)


Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(filedialog.askopenfilename())
player.set_hwnd(displayP.winfo_id())
player.set_media(Media)
player.play()
# button = tk.CTkButton(root,text="Try play video")
# button.bind("<1>",lambda self:video(display=displayP))
# button.grid(row=0,column=1)

root.mainloop()