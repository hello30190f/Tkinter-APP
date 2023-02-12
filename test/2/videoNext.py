from tkinter import filedialog
import vlc

vlcIns = vlc.MediaPlayer(filedialog.askopenfilename())
while True:
    vlcIns.play()

# https://stackoverflow.com/questions/47990695/how-to-embed-a-vlc-instance-in-a-tkinter-frame