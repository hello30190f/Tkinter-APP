import math
import customtkinter as tk

class Vector2:
    
    def __init__(self,x = 0,y = 0) -> None:
        self.x = x
        self.y = y

    def setElem(self,x,y):
        self.x = x
        self.y = y

def VectorSum(a:Vector2,b:Vector2):
    x = a.x + b.x
    y = a.y + b.y
    temp = Vector2(x,y)
    return temp




# def multiplication(a:Vector2,b:Vector2):
#     x = a.x * b.x
#     y = a.y * b.y
#     result = Vector2()