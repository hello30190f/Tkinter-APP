import math

class Vector2:
    def __init__(self,x = 0,y = 0) -> None:
        self.x = x
        self.y = y

    def setElem(self,x,y):
        self.x = x
        self.y = y


def dotProduct(a:Vector2,b:Vector2) -> list:
    """clac dot product

    Args:
        a (Vector2): Whatever you want to input
        b (Vector2): Whatever you want to input

    Returns:
        list: return dot product and cos value by tuple. index 0 is innder product. index 1 is cos value.
    """
    dot = a.x * b.x + a.y * b.y
    aLenth = VectorLenth(a)
    bLenth = VectorLenth(b)
    cos = dot / (aLenth*bLenth)
    result = (dot,cos)
    return result

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