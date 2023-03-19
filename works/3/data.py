from tkinter import messagebox

class data:

    def __init__(self) -> None:
        self.url = []
        self.title = []
        self.numberOfChar = []
        self.widgets = []

    def getInitCsvColumnNames(self):
        return "Title,URL,NumberOfChar,"

    def getData(self) -> list:
        dataTemp = []
        dataTemp.append(self.title)
        dataTemp.append(self.url)
        dataTemp.append(self.numberOfChar)
        return dataTemp

    def printData(self):
        print(self.url)
        print(self.title)
        print(self.numberOfChar)
        print(self.widgets)

    # Return only available array info
    def getArrayLenth(self) -> int:
        return len(self.url)

    # TODO: check array amount and if the number of array is worng, then fix return value.
    # Return only available array info
    def getArrayAmount(self) -> int:
        return 3

    def printDataWithTkinter(self):
        text = ""
        for lenth in range(len(self.url)):
            text += "-------------------------\n"
            text += "URL: \n" + self.url[lenth]
            text += "\nTitle: \n" + self.title[lenth]
            text += "\nCounted char amount: \n" + str(self.numberOfChar[lenth])
            text += "\nWidget: \n" + str(self.widgets[lenth])
            text += "\n\n"
        messagebox.askquestion("data",text)

    def removeElem(self,index:int):
        del self.url[index]
        del self.title[index]
        del self.numberOfChar[index]
        del self.widgets[index]
