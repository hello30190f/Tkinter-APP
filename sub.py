import customtkinter as tk
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import videoEdit
import cv2


def menu(root:tk.CTk):
    menuFrame = tk.CTkFrame(root)
    label = tk.CTkLabel(menuFrame,text="Choose what you want to use.")
    label.pack()
    frame = tk.CTkFrame(menuFrame)
    textWriter = tk.CTkButton(frame,text="Text Writer")
    textWriter.bind("<1>",lambda self:TextEditer(root))
    textWriter.grid(row=0,column=0,pady=10,padx=10)
    videoEditer = tk.CTkButton(frame,text="Video edit")
    videoEditer.bind("<1>",lambda self:videoEdit.videoEditWindow(root))
    videoEditer.grid(row=1,column=0,pady=10,padx=10)
    frame.pack()
    menuFrame.pack(padx=20,pady=20,ipadx=20,ipady=20)


def TextEditer(root:tk.CTk ):
    topWin = tk.CTkToplevel(root)
    topWin.title("Text writer")

    tabview = tk.CTkTabview(topWin)
    tabview.pack(padx=10,pady=10)
    tabview.add("Text write")
    tabview.add("Save as...")

    MainFrame = tk.CTkFrame(tabview.tab("Text write"))
    text = tk.CTkTextbox(MainFrame,height=200,width=400)
    text.grid(row=0,column=0)
    MainFrame.pack(padx=2,pady=2,sticky=tk.W+tk.S)

    SaveFrame = tk.CTkFrame(tabview.tab("Save as..."))
    SaveButton = tk.CTkButton(SaveFrame,text="Save as...")
    def saveFunc(self):
        import os
        from tkinter import filedialog
        path = filedialog.askdirectory(initialdir="./")
        checkFile = os.listdir(path=path)

        ok = True

        for item in checkFile:
            if(item == "text.txt"):
                from tkinter import messagebox
                ans = messagebox.askyesno(title="Would you like to overwrite text file?",message="There have already text.txt file.")
                ok = ans

        if(ok):
            with open(path+r"/text.txt","wt",encoding="UTF-8") as texts:
                for line in text.get("1.0",tk.END):
                    texts.write(line)


    SaveButton.bind("<1>",saveFunc)
    SaveButton.pack()
    SaveFrame.pack()

    topWin.mainloop()



def scrolledtext(root:tk.CTk):
    topWin = tk.CTkToplevel(root)

    scrolledText = tk.CTkScrollableFrame(topWin,height=200,width=500)
    entry = tk.CTkEntry(scrolledText,placeholder_text="Hello modern GUI")
    entry.pack()
    text = tk.CTkTextbox(scrolledText,width=500,height=200)
    text.pack()

    scrolledText.pack(padx=30,pady=30)

    topWin.mainloop()