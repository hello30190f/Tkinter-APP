import Web
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
import threading

def _countCharOfPTag(frame,url,row,column):
    count = Web.countPTagCharFromURL(url.get())
    label = tk.CTkLabel(frame,text="Result")
    label.grid(row=row,column=column,padx=10,pady=10)
    result = tk.CTkLabel(frame,text=str(count))
    result.grid(row=row,column=column+1,padx=10,pady=10)

def countCharOfPTag(frame,url,row,column):
    thread = threading.Thread(target=_countCharOfPTag,args=(frame,url,row,column))
    thread.start()

res = "500x500"
window_name = "char counter"
root = tk.CTk()
root.geometry(res)
root.title(window_name)

frame = tk.CTkFrame(root)
label = tk.CTkLabel(frame,text="Count p tag char number")
label.grid(row=0,column=0)
UrlEnterForm = tk.CTkEntry(frame)
UrlEnterForm.grid_configure(sticky=tk.W + tk.E)
UrlEnterForm.grid(row=1,column=0,pady=10,padx=10)
CountBegin = tk.CTkButton(frame,text="begin to count.")
CountBegin.bind("<1>",lambda args:countCharOfPTag(frame,UrlEnterForm,2,0))
CountBegin.grid(row=1,column=1,padx=10,pady=10)
frame.pack(padx=10,pady=10)



root.mainloop()