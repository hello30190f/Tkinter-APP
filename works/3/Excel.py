from openpyxl import Workbook
from tkinter import dialog
from data import data
from tkinter import filedialog


# data should be like [[1,2,3],[1,2,3]] first index is row, second index is column.
def writeData(filename:str,datas):
    path = filedialog.askdirectory()
    if(0 == len(path)):
        pass
    else:
        path += "/"
    wb = Workbook()
    ws = wb.active
    for data in datas:
        ws.append(data)
        # print(data)
    wb.save(path + filename+".xlsx")

def saveData(commonData:data):
    if(commonData.IsThereData() == False):
        return False

    temp = commonData.getData()
    datalist = []
    # print(commonData.getArrayAmount(),commonData.getArrayLenth())
    datalist.append(["Title","URL","NumberOfCharInPTag"])
    for index in range(commonData.getArrayLenth()):
        listD = []
        for indexS in range(commonData.getArrayAmount()):
            listD.append(str(temp[indexS][index]))
        datalist.append(listD)

    writeData("output",datalist)


if __name__ == "__main__":
    writeData("hello",[[1,2,3,"hello"]])