import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
import math


class lenth:

    def __init__(self,root:tk.CTk,ScreenInch = 13) -> None:
        self.ScreenWidth = root.winfo_screenwidth()
        self.ScreenHeight = root.winfo_screenmmheight()
        self.ScreenInch = ScreenInch
        self.dpi = 246
        self.OneInchToCM = 2.54 # cm

        self.CanvasWidth = 600
        self.CanvasHeight = 50

    def clacDpi(self):
        tempWidth = self.ScreenWidth ^ 2
        tempHeight = self.ScreenHeight ^ 2
        self.diagonalLenth = math.sqrt(tempWidth + tempHeight)
        picos = math.acos(self.ScreenWidth/self.diagonalLenth) #small corner
        pisin = math.asin(self.ScreenHeight/self.diagonalLenth)
        widthInch = picos * self.ScreenInch
        self.dpi = self.ScreenWidth / widthInch

    def InchToCm(self,Inch):
        return self.OneInchToCM * Inch


    def barControl(self,canvas:tk.CTkCanvas,event):
        # position = canvas.bbox(self.id)
        if(event.x >= 0 and event.x <= self.CanvasWidth - self.size):
            canvas.delete(self.id)
            self.id = canvas.create_rectangle(event.x,10,event.x+self.size,10+self.size,fill="Red")
            position = canvas.bbox(self.id)
            self.barPosition = position[0] - 10
            print(self.barPosition)


    def sliderByCanvas(self,frame:tk.CTkFrame,root:tk.CTk):
        self.size = self.CanvasHeight - 20
        canvas = tk.CTkCanvas(frame,width=self.CanvasWidth,height=self.CanvasHeight,bg="gray")
        canvas.pack(padx=10,pady=10)
        canvas.create_rectangle(10,10,self.CanvasWidth-10,self.CanvasHeight-10,fill="Green")
        self.id = canvas.create_rectangle(10,10,10+self.size,10+self.size,fill="Red")
        self.barPosition = 0  # 10 + self.size / 2
        self.barPositionOffset = 10
        canvas.bind("<B1-Motion>",lambda args:self.barControl(canvas,args))
        


    def lenthAdapter(self,root:tk.CTk):
        frame = tk.CTkFrame(root,width=self.CanvasWidth,height=self.CanvasHeight)
        self.sliderByCanvas(frame,root)
        frame.pack(pady=10,padx=10)





if __name__ == "__main__":
    res = "500x500"
    window_name = "ex"
    root = tk.CTk()
    ins = lenth(root)
    root.geometry(res)
    root.title(window_name)

    ins.lenthAdapter(root)

    root.mainloop()