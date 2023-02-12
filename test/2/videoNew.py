# import ffmpeg
from tkinter import filedialog
import time
import vlc

audio:vlc.MediaPlayer = vlc.MediaPlayer()

def audioFunc():
    global audio
    # audio = 
    audio.set_mrl(filedialog.askopenfilename())
    audio.play()

def timer():
    global audio
    while(True):
        audio.pause()
        time.sleep(2)
        audio.play()

from threading import Thread

audioTh = Thread(target=audioFunc)
audioTh.start()
timerTH = Thread(target=timer)
timerTH.start()

# video = ffmpeg.input(filedialog.askopenfilename())
# video = ffmpeg.output(video,"")

# import os

# os.system("mshta "+ "'" + filedialog.askopenfilename() + "'")