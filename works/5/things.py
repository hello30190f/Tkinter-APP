import physics
from physics import Vector2
from physics import obj
import customtkinter as tk
import math
from physics import test


# example --------------------------------------------

class exampleObj(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        obj.defineCharacter(self)

    def drawObj(self):
        obj.drawObj()

    def Updater(self):

        obj.Updater(self)

class box(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        obj.defineCharacter(self)
        self.size = 20
        self.halfSize = self.size/2
        self.upperLeft = Vector2(self.position.x-self.halfSize, self.position.y-self.halfSize)

    def Updater(self):

        obj.Updater(self)

class springs(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        obj.defineCharacter(self)

    def Updater(self):

        obj.Updater(self)

class glue(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        obj.defineCharacter(self)

    def Updater(self):

        obj.Updater(self)

class stick(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        obj.defineCharacter(self)

    def Updater(self):

        obj.Updater(self)


# example --------------------------------------------



if __name__ == "__main__":
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass
    res = "500x500"
    window_name = "ex"
    root = tk.CTk()
    root.geometry(res)
    root.title(window_name)

    test(root)


    root.mainloop()