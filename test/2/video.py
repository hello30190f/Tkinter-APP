from tkinter import filedialog
import cv2
import numpy as np
import time
# from ffmpeg import stream,audio,video,image
# from playsound import playsound

import moviepy.editor as mp
from threading import Thread


# file = filedialog.askopenfiles("rb",filetypes=["all files","video .mp4"])
filePath = filedialog.askopenfilename()

# Aaudio = audio.


clip = mp.VideoFileClip(filePath)
AudioFilePath = filePath.replace(".mp4",".wav")
import os
if(os.path.isfile(AudioFilePath) != True):
    clip.audio.write_audiofile(AudioFilePath)
# playsound(AudioFilePath)

stopFlag = False
sampleFrame = None
import vlc


def playsound():
    audioPlayer = vlc.MediaPlayer()
    audioPlayer.set_mrl(AudioFilePath)
    global sampleFrame
    oneTimeFlag = False
    audioPlayer.play()

    # while True:
        # temp = sampleFrame
        # time.sleep(0.2)
        # if(temp.all() != None):
            # if(temp.any() == sampleFrame.any()):
                # audioPlayer.pause()
                # oneTimeFlag = False
            # else:
                # if (oneTimeFlag == False):
                    # audioPlayer.play()
                    # oneTimeFlag = True
            # pass

def videoPlay():

    Avideo = cv2.VideoCapture(filePath)
    fps = Avideo.get(cv2.CAP_PROP_FPS)
    print(fps)
    OneFrameTime = 1/fps
    deltaTime = time.time()
    global sampleFrame
    import customtkinter as ctk
    from PIL import Image,ImageTk

    def init(root:ctk.CTk):
        if(Avideo.isOpened()):
            r,f = Avideo.read()
            # canvas = ctk.CTkCanvas(root,width=)

    def play(self):
        while(Avideo.isOpened()):

            ret,frame = Avideo.read()
            colorCon = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            framePil = Image.fromarray(colorCon)
            imagetk = ImageTk.PhotoImage(framePil)
            
            
            # getFrame(frame=frame)
            # sampleFrame = frame

            if ret == False:
                break

            # cv2.imshow("frame",frame)
            # time.sleep(OneFrameTime)

            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break


        # Avideo.release()
        # cv2.destroyAllWindows()

    root = ctk.CTk()

    button = ctk.CTkButton(root,text="play",command=play)
    button.pack()

    root.mainloop()





def precessStopDitector(frame):
    temp = frame
    time.sleep(0.5)
    if(temp == frame):
        stopFlag = True
        print("work")
    else:
        stopFlag = False



if __name__ == "__main__":
    # AudioThread = Thread(target=playsound)
    # AudioThread.start()
    # VideoThread = Thread(target=videoPlay)
    # VideoThread.start()
    # StopDitect = Thread(target=precessStopDitector,args=[sampleFrame])
    # StopDitect.start()

    audioPlayer = vlc.MediaPlayer()
    audioPlayer.set_mrl(filePath)
    audioPlayer.play()
