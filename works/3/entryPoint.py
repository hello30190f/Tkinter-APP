import Web
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
import threading


class func:
    _historyIndex = 0
    _content = []

    def _removeElem(self,elemList):
        conter = 0
        for elem in elemList:
            elem:tk.CTkLabel
            elem.destroy()
            conter += 1

    def _removeSelectedElem(self):
        conter = 0
        for elem in self._content:
            if(self._content[conter][0].get() == "on"):
                self._removeElem(elem)
                del self._content[conter]
            conter += 1

    def _countCharOfPTag(self,frame,url,row,column):
        temp = []
        count = Web.countPTagCharFromURL(url.get())
        select = tk.CTkCheckBox(frame,onvalue="on",offvalue="off",text="")
        select.grid(row=row+self._historyIndex,column=column)
        label = tk.CTkLabel(frame,text="Result")
        label.grid(row=row+self._historyIndex,column=column+1,padx=10,pady=10)
        result = tk.CTkLabel(frame,text=str(count))
        result.grid(row=row+self._historyIndex,column=column+2,padx=10,pady=10)
        temp.append(select)
        temp.append(label)
        temp.append(result)
        self._content.append(temp)
        self._historyIndex += 1

    def countCharOfPTag(self,frame,url,row,column):
        thread = threading.Thread(target=self._countCharOfPTag,args=(frame,url,row,column))
        thread.start()

    def removeButton(self,root):
        delete = tk.CTkButton(root,text="remove selected result")
        delete.bind("<1>",lambda args:self._removeSelectedElem())
        delete.pack()


funcTools = func()
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
CountBegin.bind("<1>",lambda args:funcTools.countCharOfPTag(frame,UrlEnterForm,2,0))
CountBegin.grid(row=1,column=1,padx=10,pady=10)
frame.pack(padx=10,pady=10)

funcTools.removeButton(root)



root.mainloop()