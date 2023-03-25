import customtkinter as tk
class value:

    result = ""

    def __init__(self,explain = "Please enter",windowName = "Entry form") -> None:
        import ctypes
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
        except:
            pass
        # import customtkinter as tk
        # res = "500x500"
        window_name = windowName
        root = tk.CTk()
        # root.geometry(res)
        root.title(window_name)


        label = tk.CTkLabel(root,text=explain)
        label.pack()
        Entry = tk.CTkEntry(root,width=400)
        Entry.bind("<Return>",lambda args:self.getEntryValue(root,Entry))
        Entry.pack()

        root.mainloop()

    def getEntryValue(self,root:tk.CTk,Entry:tk.CTkEntry):
        self.result = Entry.get()
        root.quit()


if __name__ == "__main__":
    ins = value()
    print(ins.result)