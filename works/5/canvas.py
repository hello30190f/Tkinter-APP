import customtkinter as tk
import time
import math


class timer:
    
    def __init__(self):
        self.time = time.time()
        self.prevTime = 0
        self.delta = 0

    def UpdateMe(self):
        self.delta = time.time() - self.prevTime
        self.prevTime = time.time()

class repeatPart:

    def __init__(self,canvas:tk.CTkCanvas,Interval = 16) -> None:
        import pyhsics
        from pyhsics import Vector2
        self.Interval = Interval
        self.canvas = canvas

        pass

    def UpdateMe(self):
        pass


class boxAndPhysics:

    def _resizeEnevtHandler(self,root:tk.CTk,canvas:tk.CTkCanvas):
        canvas.configure(width=root.winfo_width(),height=root.winfo_height())

    def __init__(self,root:tk.CTk):
        # timeClac = timer()
        self.TimeRepeat = 16 # about 60 fps
        self.canvas = tk.CTkCanvas(root,width=root.winfo_width(),height=root.winfo_height(),bg="gray")
        self.canvas.pack(padx=10,pady=10)
        self.canvas.bind("<1>",lambda event:self._canvasHandlerMousePressed(event))
        self.canvas.bind("<B1-Motion>",lambda event:self._canvasHandlerMouseMoving(event))
        self.canvas.bind("<ButtonRelease-1>",lambda event:self._canvasHandlerMouseReleased(event))
        root.bind("<Configure>",lambda event:self._resizeEnevtHandler(root,self.canvas))
        root.after(self.TimeRepeat,self._repeat(root))
        self.x = 10
        self.y = 10
        self.size = 50
        self.halfSize = int(self.size/2)
        self.PrevCanvas = None
        self.repeatPart = repeatPart(self.canvas,self.TimeRepeat)

    def _repeat(self,root):
        root.after(16,self._repeat(root))
        self.repeatPart.UpdateMe()

    def _canvasHandlerMousePressed(self,event):
        self._drawBox(event.x,event.y)
        # print("press")
        pass

    def _canvasHandlerMouseMoving(self,event):
        self._drawBox(event.x,event.y)
        # print(event.x)
        pass

    def _canvasHandlerMouseReleased(self,event):
        # print("release")
        pass

    def _returnRectSize(self,x,y):
        return x,y,x+self.size,y+self.size

    def _drawBox(self,x,y):
        self.canvas:tk.CTkCanvas
        if(self.PrevCanvas == None):
            pass
        else:
            self.canvas.delete(self.PrevCanvas)
        self.PrevCanvas = self.canvas.create_rectangle( x- self.halfSize,
                                                        y- self.halfSize,
                                                        x+ self.size -self.halfSize,
                                                        y+ self.size -self.halfSize,
                                                        fill="Red")


