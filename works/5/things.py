import physics
from physics import Vector2
from physics import obj
import customtkinter as tk
import math
from physics import test


class box(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        self.position = Vector2()

class springs(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        self.position = Vector2()

class glue(obj):
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        self.position = Vector2()

class stick:
    def __init__(self, root: tk.CTk) -> None:
        super().__init__(root)

    def defineCharacter(self):
        self.position = Vector2()



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