

def test1():
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass
    import customtkinter as tk
    res = "500x500"
    window_name = "ex"
    root = tk.CTk()
    root.geometry(res)
    root.title(window_name)

    def ifsentence(value):
        if("on" == value):
            print("on")
        else:
            print("off")



    select = tk.CTkCheckBox(root,onvalue="on",offvalue="off",text="")
    select.pack()
    printbutton = tk.CTkButton(root,text="print value of checkbox")
    printbutton.bind("<1>",lambda args:ifsentence(select.get()))
    printbutton.pack()

    root.mainloop()


if __name__ == "__main__":
    from tkinter import filedialog

    filepath = filedialog.askdirectory()
    print(filepath)
