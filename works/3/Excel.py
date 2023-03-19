from openpyxl import Workbook
from tkinter import dialog
from data import data


# data should be like [[1,2,3],[1,2,3]] first index is row, second index is column.
def writeData(filename:str,datas):
    wb = Workbook()
    ws = wb.active
    for data in datas:
        ws.append(data)
        # print(data)
    wb.save(filename+".xlsx")

def saveData(commonData:data):
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
    writeData("hello")