import Web
import Excel
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
import threading
from data import data
from tkinter import messagebox


class func:
    _historyIndex = 0
    _content = []

    def _removeElem(self,elemList):
        counter = 0
        for elem in elemList:
            elem:tk.CTkLabel
            elem.destroy()
            counter += 1

    def _removeSelectedElem(self,commonData:data):
        counter = 0
        for elem in self._content:
            if(self._content[counter][0].get() == "on"):
                self._removeElem(elem)
                del self._content[counter]
                commonData.removeElem(counter)
            counter += 1

    def _countCharOfPTag(self,frame,url,row,column,commonData:data):
        temp = []
        count,title = Web.countPTagCharFromURL(url.get())
        commonData.title.append(title)
        commonData.numberOfChar.append(count)
        commonData.url.append(url.get())
        select = tk.CTkCheckBox(frame,onvalue="on",offvalue="off",text="",checkbox_width=20,checkbox_height=20,width=20)
        select.grid(row=row+self._historyIndex,column=column)
        label = tk.CTkLabel(frame,text=title)
        label.grid(row=row+self._historyIndex,column=column+1,padx=10,pady=10)
        result = tk.CTkLabel(frame,text=str(count))
        result.grid(row=row+self._historyIndex,column=column+2,padx=10,pady=10)
        temp.append(select)
        temp.append(label)
        temp.append(result)
        commonData.widgets.append(temp)
        self._content.append(temp)
        self._historyIndex += 1



    def countCharOfPTag(self,frame,url,row,column,commonData:data):
        # commonData.url.append(url.get())
        thread = threading.Thread(target=self._countCharOfPTag,args=(frame,url,row,column,commonData))
        thread.start()

    def removeButton(self,root,commonData:data):
        delete = tk.CTkButton(root,text="remove selected result")
        delete.bind("<1>",lambda args:self._removeSelectedElem(commonData))
        delete.pack(padx=10,pady=10,side=tk.LEFT)

    def saveButton(self,root,commonData:data):
        save = tk.CTkButton(root,text="Save data")
        save.bind("<1>",lambda args:Excel.saveData(commonData))
        save.pack(padx=10,pady=10,side=tk.LEFT)
        
    def printData(self,root,commonData:data):
        dataPrint = tk.CTkButton(root,text="Print data")
        dataPrint.bind("<1>",lambda args:commonData.printDataWithTkinter())
        dataPrint.pack(padx=10,pady=10)

    # def DataExistenceCheck(self,root,commonData:data):
    #     check = tk.CTkButton(root,text="check existence of data")
    #     check.bind("<1>",lambda args:commonData.IsThereData())
    #     check.pack(padx=10,pady=10)





if __name__ == "__main__":

    commonData = data()
    funcTools = func()
    # res = "500x500"
    window_name = "char counter"
    root = tk.CTk()
    # root.geometry(res)
    root.title(window_name)

    frame = tk.CTkFrame(root)
    label = tk.CTkLabel(frame,text="Count p tag char number")
    label.grid(row=0,column=0)
    UrlEnterForm = tk.CTkEntry(frame)
    UrlEnterForm.grid_configure(sticky=tk.W + tk.E)
    UrlEnterForm.grid(row=1,column=0,pady=10,padx=10)
    CountBegin = tk.CTkButton(frame,text="begin to count.")
    CountBegin.bind("<1>",lambda args:funcTools.countCharOfPTag(frame,UrlEnterForm,2,0,commonData))
    CountBegin.grid(row=1,column=1,padx=10,pady=10,sticky=tk.W)
    frame.pack(padx=10,pady=10)


    frame2 = tk.CTkFrame(root)
    funcTools.printData(frame2,commonData)
    funcTools.removeButton(frame2,commonData)
    funcTools.saveButton(frame2,commonData)
    frame2.pack(pady=(0,10))
    




    root.mainloop()