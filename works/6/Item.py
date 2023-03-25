class elemSelector:

    def __init__(self) -> None:
        self.content = []

    # [ID,value],[same thing], ...
    def setContent(self,ID,value):
        temp = []
        temp.append(ID)
        temp.append(value)
        self.content.append(temp)



class scriptData:

    def __init__(self) -> None:
        self.content = []

    def setScript(self,scriptString:str):
        self.content.append(scriptString)


class waitTime:

    def __init__(self) -> None:
        self.content = []
    
    def setTime(self,time):
        self.content.append(float(time))