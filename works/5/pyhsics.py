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
        self.canvasId = canvasId
        self.canvas = canvas
        self.position = self.getMiddlePosition()

    def getMiddlePosition(self) -> Vector2:
        positionEdges = self.canvas.bbox(self.canvasId)
        width = positionEdges[2] - positionEdges[0]
        height = positionEdges[3] - positionEdges[1]
        Xmiddle = positionEdges[0] + width/2
        Ymiddle = positionEdges[1] + height/2
        middle = Vector2(Xmiddle,Ymiddle)
        return middle

    def updatePosition(self):
        self.position = self.getMiddlePosition()

    def UpdateCanvasId(self,CanvasId):
        self.canvas = CanvasId

    def UpdateMe(self,canvasId):
        self.updatePosition()
        self.UpdateCanvasId(canvasId)

class spring:

    def __init__(self,lenth = 10,constant = 1) -> None:
        self.lenth = lenth
        self.constant = constant

# -----------------------------------------------------------------------

def VectorSum(a:Vector2,b:Vector2) -> Vector2:
    x = a.x + b.x
    y = a.y + b.y
    temp = Vector2(x,y)
    return temp

def VectorSub(a:Vector2,b:Vector2) -> Vector2:
    temp = Vector2(-b.x,-b.y)
    return VectorSum(a,temp)

def VectorLenth(a:Vector2) -> float:
    lenth = math.sqrt(a.x^2 + a.y^2)
    return lenth


# -----------------------------------------------------------------------

class physicsClac:

    def positionDiff(a:Vector2,b:Vector2):
        temp = Vector2((a.x - b.x),(a.y - b.y))


    def clacSpringForce(self,Pa:obj,Pb:obj,springC:spring,Interval = 16) -> list:
        ForceAx = springC.constant * (Pb.position.x - Pa.position.x)
        ForceAy = springC.constant * (Pb.position.y - Pa.position.y) # y axis inverted

        ForceBx = springC.constant * (Pa.position.x - Pb.position.x)
        ForceBy = springC.constant * (Pa.position.y - Pb.position.y)

        A = Vector2(ForceAx,ForceAy)
        B = Vector2(ForceBx,ForceBy)
        result = [A,B]

        return result

    def clacAcceraration(self,Pa:obj,Pb:obj,springC:spring,Interval = 16) -> list:
        force = self.clacSpringForce(Pa,Pb,springC,Interval)
        A = force[0] 
        A:Vector2
        B = force[1]
        B:Vector2

        A.x = A.x / Pa.mass
        A.y = A.y / Pa.mass

        B.x = B.x / Pb.mass
        B.y = B.y / Pb.mass

        result = [A,B]
        return result



# -----------------------------------------------------------------------







# -----------------------------------------------------------------------

def clacForce(canvas:tk.CTkCanvas,Pa:obj,Pb:obj,springC:spring,Interval = 16):
    ForceA = -springC.constant
    pass



# def multiplication(a:Vector2,b:Vector2):
#     x = a.x * b.x
#     y = a.y * b.y
#     result = Vector2()