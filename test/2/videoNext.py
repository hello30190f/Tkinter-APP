from tkinter import filedialog
import vlc

vlcIns = vlc.MediaPlayer(filedialog.askopenfilename())
while True:
    vlcIns.play()