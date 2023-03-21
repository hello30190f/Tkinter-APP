import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk



class function:

    def __init__(self,root:tk.CTk) -> None:
        self.root = root
        self.result = ""
        self.width = 600
        self.height = 1

    def processPath(self,path):
        for char in path:
            if(char == "\\"):
                self.result += "\\" + char
            else:
                self.result += char

    def drawPath(self,frame:tk.CTkFrame):
        text = tk.CTkTextbox(frame,height=self.height)
        text.insert(1.0,self.result)
        text.pack()
        text.configure(state="disabled",width=self.width)

    def CleanResult(self):
        if(self.result == ""):
            pass
        else:
            self.result = ""

    def precessAnShowPath(self,path,frame):
        self.CleanResult()
        self.processPath(path)
        self.drawPath(frame)

    def showForm(self):
        self.frame = tk.CTkFrame(self.root)
        self.label = tk.CTkLabel(self.frame,text="Enter path")
        self.label.grid(row=0,column=0,sticky=tk.W,padx=16)
        self.entry = tk.CTkEntry(self.frame,width=self.width)
        resultFrame = tk.CTkFrame(self.frame,width=self.width,height=0)
        resultFrame.grid(row=2,column=0,pady=10)
        self.entry.bind("<Return>",lambda args:[self.precessAnShowPath(self.entry.get(),resultFrame)])
        self.entry.grid(padx=10,row=1,column=0,sticky=tk.E+tk.W)
        self.frame.pack(padx=10,pady=10,anchor=tk.W)




if __name__ == "__main__":
    # res = "500x500"

    window_name = "Path modify"
    root = tk.CTk()
    func = function(root)
    # root.geometry(res)
    root.title(window_name)

    func.showForm()

    root.mainloop()