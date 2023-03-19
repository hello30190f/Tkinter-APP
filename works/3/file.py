import os

def findfile(filename:str,extention:str,path="./") -> bool:
    find = False
    filelist = os.listdir(path=path)
    for file in filelist:
        temp = list(file.split(sep=".",maxsplit=1))
        if(temp.__len__ == 1):
            if(filename == temp[0]):
                find = True
        else:
            if(filename == temp[0] and extention == temp[1]):
                find = True
    return find



def openFile(filename:str,extension:str,path="./"):
    if findfile(filename=filename,extention=extension,path=path):
        
        pass





if __name__ == "__main__":
    # result = findfile("hello","xlsx")
    result = findfile("Web","xlsx")
    print(result)
    