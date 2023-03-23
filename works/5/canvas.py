import customtkinter as tk
import time


class physics:
    


    def __init__(self,massA = 10,lenth = 1,K = 2) -> None:
        self.massA = massA # Kg
        self.lenth = lenth # m
        self.constantK = K # N/m
        self.time = 0 
    
    def _deltaTime(self):
        pass

    def _clacMovement(self):
        
        
        pass


class boxAndPhysics:

    def _resizeEnevtHandler(self,root:tk.CTk,canvas:tk.CTkCanvas):
        canvas.configure(width=root.winfo_width(),height=root.winfo_height())

    def __init__(self,root:tk.CTk):
        self.canvas = tk.CTkCanvas(root,width=root.winfo_width(),height=root.winfo_height(),bg="gray")
        self.canvas.pack(padx=10,pady=10)
        self.canvas.bind("<1>",lambda event:self._canvasHandlerMousePressed(event))
        self.canvas.bind("<B1-Motion>",lambda event:self._canvasHandlerMouseMoving(event))
        self.canvas.bind("<ButtonRelease-1>",lambda event:self._canvasHandlerMouseReleased(event))
        root.bind("<Configure>",lambda event:self._resizeEnevtHandler(root,self.canvas))
        self.x = 10
        self.y = 10
        self.size = 50
        self.halfSize = int(self.size/2)
        self.PrevCanvas = None

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


