import time
import customtkinter as tk
from vector2 import Vector2


class obj:
    # self.time can be used to clac object physics
    def timer(self):
        self.root:tk.CTk
        self.time += time.time() - self.prevTime
        self.prevTime = time.time()
        self.root.after(16,lambda :self.timer())

    def defineCharacter(self):
        self.position = Vector2()

    # Call this function at the end of your code when you override this.
    def Updater(self):
        self.drawObj()
        self.root.after(16,lambda :self.Updater())

    def _resizeEnevtHandler(root:tk.CTk,canvas:tk.CTkCanvas):
        canvas.configure(width=root.winfo_width(),height=root.winfo_height())

    # This function should be called when Updater function is executed.
    def drawObj(self):
        self.canvas = tk.CTkCanvas(self.root,width=self.root.winfo_width(),height=self.root.winfo_height())
        self.root.bind("<Configure>",lambda tets:self._resizeEnevtHandler(self.root,self.canvas))

    def __init__(self,root:tk.CTk) -> None:
        self.time = 0
        self.prevTime = time.time()
        self.root = root
        self.timer()
        self.defineCharacter()


class property:
    def __init__(self) -> None:
        pass

    def defineGravity(self):
        self.gravity = 9.8 #m/s^2

    def defineDrag(self):
        self.airDrag = 0


def test(root:tk.CTk):
    Ins = obj(root)
    currentTime = tk.DoubleVar(root,int(Ins.time))
    def Update():
        currentTime.set(int(Ins.time))
        root.after(16,lambda :Update())
    root.after(16,lambda :Update())
    showTime = tk.CTkLabel(root,textvariable=currentTime)
    showTime.pack()



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