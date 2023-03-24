import time
import customtkinter as tk

class obj:

    def __init__(self,root:tk.CTk) -> None:
        self.time = 0
        self.prevTime = time.time()
        self.root = root
        self.timer()

    def timer(self):
        self.root:tk.CTk
        self.time += time.time() - self.prevTime
        self.prevTime = time.time()
        self.root.after(16,lambda :self.timer())

    



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