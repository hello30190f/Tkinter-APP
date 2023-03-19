from tkinter import messagebox

class data:

    def __init__(self) -> None:
        self.url = []
        self.title = []
        self.widgets = []

    def printData(self):
        print(self.url)
        print(self.title)
        print(self.widgets)

    def printDataWithTkinter(self):
        text = ""
        for lenth in range(len(self.url)):
            text += "URL: " + self.url[lenth]
            text += " Title: " + self.title[lenth]
            text += " Widget: " + str(self.title[lenth])
            text += "\n"
        messagebox.askquestion("data",text)

    def removeElem(self,index:int):
        del self.url[index]
        del self.title[index]
        del self.widgets[index]
