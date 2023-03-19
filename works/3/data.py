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
            text += "-------------------------\n"
            text += "URL: \n" + self.url[lenth]
            text += "\nTitle: \n" + self.title[lenth]
            text += "\nWidget: \n" + str(self.widgets[lenth])
            text += "\n\n"
        messagebox.askquestion("data",text)

    def removeElem(self,index:int):
        del self.url[index]
        del self.title[index]
        del self.widgets[index]
