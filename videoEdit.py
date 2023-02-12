import customtkinter as tk
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import cv2
from PIL import Image
import configparser as iniReader

def videoRead():
    from tkinter import filedialog
    import os
    path = filedialog.askdirectory(initialdir="./") + "/"
    itemNames = os.listdir()
    filePath = []
    for item in itemNames:
        if(".mp4" in item):
            filePath.append(path + item)
    video = []
    for file in filePath:
        video.append(cv2.VideoCapture(file))
    
    pass

def videoWrite():
    pass

def timeLine():
    pass

def controlPanel():
    pass

videoKeeper = []
windowSettingIntegrated = True

def _configRead():
    Targetconf = []
    iniFs = iniReader.ConfigParser()
    configPath = "./videoEdit.ini"
    iniFs.read(configPath)
    windowSettingIntegratedTemp = iniFs.get("UserSetting","windowSettingIntegrated")
    if(windowSettingIntegratedTemp == "True"):
        Targetconf.append(True)
    else:
        Targetconf.append(False)
    return Targetconf

def _configWriteAndRead():
    import os
    isThereConfigFile = True
    items = os.listdir("./")
    for item in items:
        if(item == "videoEdit.ini"):
            isThereConfigFile = True
            break
        else:
            isThereConfigFile = False

    if(isThereConfigFile == False):
        iniFs = iniReader.ConfigParser()
        iniFs["UserSetting"]={"windowSettingIntegrated":True}
        iniFs["default"]={"windowSettingIntegrated":True}
        with open("videoEdit.ini","w") as setting:
            iniFs.write(setting) 
    else:
        returnedValue = _configRead()
    return returnedValue

def videoEditWindow(root:tk.CTk):
    settinglist = _configWriteAndRead()
    windowSettingIntegrated = settinglist[0]

    if(windowSettingIntegrated):
        _videoEditWindowIntegrated(root)
    else:
        _videoEditWindowSeparated(root)
        pass




def _videoEditWindowSeparated(root:tk.CTk):
    VideoViewWindow = tk.CTkToplevel(root)


    VideoViewWindow.mainloop()
    pass





def _videoEditWindowIntegrated(root:tk.CTk):
    VideoEditWin = tk.CTkToplevel(root)
    VideoEditWin.title("Video editer")
    VideoEditWin.resizable(width=False,height=False)
    # VideoEditWin.geometry("300x300")

    videoEditTab = tk.CTkTabview(VideoEditWin)
    videoEditTab.pack()
    videoEditTab.add("video edit")
    videoEditTab.add("settings")

    videoFrameWidth = int(1600/2)
    VideoEditFrame = tk.CTkFrame(videoEditTab.tab("video edit"))
    videoFrame = tk.CTkFrame(VideoEditFrame,height=450,width=videoFrameWidth)
    videoFrame.grid(row=0,column=0,padx=5,pady=5)
    TimeLine = tk.CTkFrame(VideoEditFrame,width=videoFrameWidth,height=200)
    TimeLine.grid(row=1,column=0,padx=5,pady=5)
    VideoEditFrame.grid(row=0,column=0,sticky=tk.S,padx=6,pady=6)

    ControlPanel = tk.CTkFrame(videoEditTab.tab("video edit"))
    ControlPanel.grid(rowspan=2,row=0,column=1,sticky=tk.NS,padx=5,pady=6)


    VideoEditWin.mainloop()

    pass


