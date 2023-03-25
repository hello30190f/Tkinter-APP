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

ItemVar = tk.StringVar(root,"test1")
menu = tk.CTkOptionMenu(root,
                        values=["test1","test2"],
                        variable=ItemVar)
# menu.bind("<1>",lambda args:print(menu.get()))
menu.pack()

printButton = tk.CTkButton(root,text="printText")
printButton.bind("<1>",lambda args:print(ItemVar.get()))
printButton.pack()


def test():
    test = textBox.get(1.0,tk.END)
    print(test)

textBox = tk.CTkTextbox(root,width=200,height=200)
textBox.bind("<Return>",lambda args:test())
textBox.pack()



root.mainloop()