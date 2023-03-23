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


    def barControl(self,canvas:tk.CTkCanvas,id):
        
        pass


    def sliderByCanvas(self,frame:tk.CTkFrame):
        canvas = tk.CTkCanvas(frame,width=frame.winfo_width(),height=frame.winfo_height(),bg="gray")
        canvas.pack(padx=10,pady=10)
        canvas.create_rectangle(10,10,frame.winfo_width-10,frame.winfo_height-10,fill="Green")
        self.size = frame.winfo_height - 20
        id = canvas.create_rectangle(10,10,self.size+10,self.size+10)
        canvas.bind("<B1-Motion>",lambda args:self.barControl(canvas,id))
        


    def lenthAdapter(self,root:tk.CTk):
        frame = tk.CTkFrame(root)


        frame.pack(pady=10,padx=10)
        pass





if __name__ == "__main__":
    res = "500x500"
    window_name = "ex"
    root = tk.CTk()
    root.geometry(res)
    root.title(window_name)


    root.mainloop()