from openpyxl import Workbook
from tkinter import dialog


# data should be like [[1,2,3],[1,2,3]] first index is row, second index is column.
def writeData(filename:str,datas):
    wb = Workbook()
    ws = wb.active
    for data in datas:
        ws.append(data)
    wb.save(filename+"xlsx")

if __name__ == "__main__":
    writeData("hello")