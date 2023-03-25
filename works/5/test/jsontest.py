import json
from tkinter import filedialog

def readJson():
    result = None
    result:dict
    with filedialog.askopenfile("r") as file:
        result = json.load(file)
        # print(result)

    # print(result["A things"])
    # print(result.keys().__str__())
    # temp = result[result.keys().__str__()]

    # for test in result:
    #     # print(test)
    #     for elem in result[test]:
    #         print(elem)

        readDict(result)
    

def readDict(data:dict):
    resultArray = []
    temp = []
    def readDictR(data:dict):
        try:
            for elem in data:
                resultArray.append(elem)
                temp.append(data.values())
                readDictR(data[elem])
        except:
            pass
    readDictR(data)
    print(resultArray)
    # print(temp)
    for text in temp:
        print(text)
        print()





readJson()