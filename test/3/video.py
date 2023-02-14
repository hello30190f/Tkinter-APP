import customtkinter as tk
import tkinter as btk
from tkinter import filedialog
import vlc
import cv2


_UpdateInterval = 200 # ms

class videoPlayer:
    # super()

    def createPlayer(self,Targetwidget:tk.CTkFrame):
        vlcInstance = vlc.Instance()
        mediaPlayer = vlcInstance.media_player_new()
        media = vlcInstance.media_new(filedialog.askopenfilename())
        mediaPlayer.set_hwnd(Targetwidget.winfo_id())
        mediaPlayer.set_xwindow(Targetwidget.winfo_id())
        mediaPlayer.set_media(media)
        return mediaPlayer,media

    def _playPosition(self,vlcIns,position:float):
        if(vlcIns.get_state() == vlc.State.Paused):
            vlcIns.set_position(position)
        else:
            vlcIns.pause()
            vlcIns.set_position(position)
            vlcIns.play()



    def _SelectNextVideo(self,vlcIns):
        posi = vlcIns.get_position
        print(posi)

    # https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
    # https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.html
    # "event-event" 組み合わせ bind

    def _basicControlPanel(self,root:tk.CTkToplevel,vlcInstance,mediaObj):
        KeyPressedF = False
        controlFrame = tk.CTkFrame(root)
        playButton = tk.CTkButton(controlFrame,text="Play")
        playButton.bind("<1>",lambda self:vlcInstance.play())
        playButton.grid(padx=10,pady=10,row=0,column=1)
        stopButton = tk.CTkButton(controlFrame,text="Stop/Play")
        stopButton.bind("<1>",lambda self:vlcInstance.pause())
        stopButton.grid(padx=10,pady=10,row=0,column=2)
        videoPlayPosition = tk.StringVar(controlFrame,"0")
        videoLength = mediaObj.get_duration()
        initUpdate = True
        import math
        import numpy as np
        def _updateTimeLabelAndSliderPosition(controlFrame:tk.CTkFrame,TimeSlider:tk.CTkSlider,vlcIns,timeStr:tk.DoubleVar,mediaObj):
            videoLength = mediaObj.get_duration()
            time = vlcIns.get_position()
            TimeSlider.set(time)
            if(initUpdate):
                videoSec = abs(videoLength/1000)
            WholeMinute = math.floor(videoSec/60)
            WholeSec = math.floor(videoSec % 60)
            WholeSec = f"{WholeSec:02}"
            WholeVideoTime = str(WholeMinute) + ":" + str(WholeSec)
            CurrntSecM:float = abs(videoSec * time)
            CurrntSec = math.floor(CurrntSecM % 60)
            CurrntMin = math.floor(CurrntSecM/60)
            videoTime = WholeVideoTime + " / " + str(CurrntMin) + ":" + f"{CurrntSec:02}"
            timeStr.set(videoTime)
            controlFrame.after(_UpdateInterval,lambda :_updateTimeLabelAndSliderPosition(controlFrame,slideBar,vlcInstance,videoPlayPosition,mediaObj))
        controlFrame.after(_UpdateInterval,lambda :_updateTimeLabelAndSliderPosition(controlFrame,slideBar,vlcInstance,videoPlayPosition,mediaObj))
        slideBar = tk.CTkSlider(controlFrame,width=100,height=10,from_=0,to=1)
        slideBar.set(0)
        slideBar.bind("<B1-Motion>",lambda test:self._playPosition(vlcInstance,slideBar.get()))
        slideBar.bind("<1>",lambda test:self._playPosition(vlcInstance,slideBar.get()))
        slideBar.grid(padx=10,pady=10,row=0,column=3)
        positionLabel = tk.CTkLabel(controlFrame,textvariable=videoPlayPosition)
        positionLabel.grid(padx=10,pady=10,row=0,column=0)
        controlFrame.pack(padx=10,pady=10)

    def _resizeEvent(self,widgetList:list):
        # root.bind("<Configure>",lambda self:_re)
        vlcIns:tk.CTkFrame = widgetList[1]
        window:tk.CTkToplevel = widgetList[0]
        vlcIns.configure(True,width=int(window.winfo_width()/2.5),height=int(window.winfo_height()/3))
        pass

    def _PlayerInstanceDelete(self,vlcIns,windowins:tk.CTkToplevel):
        vlcIns.pause()
        windowins.destroy()
        vlcIns.stop()

    def MainPlayer(self,root:tk.CTk):
        playerWindow = tk.CTkToplevel(root)
        playerWindow.title("Player")
        videoFrame = tk.CTkFrame(playerWindow,width=600,height=300)
        videoFrame.pack()
        vlcIns,media = self.createPlayer(videoFrame)
        playerWindow.protocol("WM_DELETE_WINDOW",lambda :self._PlayerInstanceDelete(vlcIns,playerWindow))
        self._basicControlPanel(playerWindow,vlcIns,media)
        playerWindow.bind("<Configure>",lambda tete:self._resizeEvent([playerWindow,videoFrame,vlcIns]))
        playerWindow.mainloop()



if __name__ == "__main__":
    res = "500x500"
    window_name = "Dev instance"
    root = tk.CTk()
    root.geometry(res)
    root.title(window_name)

    LaunchLabel = tk.CTkFrame(root)
    LaunchLabel.pack(pady=10,padx=10,anchor=tk.W)
    LaunchButton = tk.CTkButton(LaunchLabel,text="Launch player")
    playerIns = videoPlayer()
    LaunchButton.bind("<1>",lambda test:playerIns.MainPlayer(root))
    LaunchButton.grid(padx=10,pady=10,row=0,column=0)

    root.mainloop()