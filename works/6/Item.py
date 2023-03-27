class elemSelector:

    def __init__(self) -> None:
        self.content = []

    # [tag,ID,value],[same thing], ...
    def setContent(self,tag,ID,value):
        temp = []
        temp.append(tag)
        temp.append(ID)
        temp.append(value)
        self.content.append(temp)



class scriptData:

    def __init__(self) -> None:
        self.content = []

    # [tag,stringOfScript],[same thing], ...
    def setScript(self,tag,scriptString:str):
        temp = []
        temp.append(tag)
        temp.append(scriptString)
        self.content.append(temp)


class waitTime:

    def __init__(self) -> None:
        self.content = []

    # [tag,time(float)],[same thing], ...
    def setTime(self,tag,time):
        temp = []
        temp.append(tag)
        temp.append(float(time))
        self.content.append(temp)