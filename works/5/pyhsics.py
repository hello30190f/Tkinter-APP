import math
import customtkinter as tk

class Vector2:
    
    def __init__(self,x = 0,y = 0) -> None:
        self.x = x
        self.y = y

    def setElem(self,x,y):
        self.x = x
        self.y = y

class obj:

    def __init__(self,canvas:tk.CTkCanvas,canvasId,mass = 1,x = 0, y = 0) -> None:
        self.mass = 1
        self.position = Vector2(x,y)
        self.canvasId = canvasId
        self.canvas = canvas

    def getMiddlePosition(self):
        positionEdges = self.canvas.bbox(self.canvasId)
        width = positionEdges[2] - positionEdges[0]
        height = positionEdges[3] - positionEdges[1]
        Xmiddle = positionEdges[0] + width/2
        Ymiddle = positionEdges[1] + height/2
        middle = Vector2(Xmiddle,Ymiddle)
        return middle

    def UpdateCanvasId(self,CanvasId):
        self.canvas = CanvasId

def VectorSum(a:Vector2,b:Vector2):
    x = a.x + b.x
    y = a.y + b.y
    temp = Vector2(x,y)
    return temp

def clacForce(canvas:tk.CTkCanvas):
    
    pass



# def multiplication(a:Vector2,b:Vector2):
#     x = a.x * b.x
#     y = a.y * b.y
#     result = Vector2()