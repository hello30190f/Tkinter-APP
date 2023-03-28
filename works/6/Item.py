class opration:
    selectElem = "Select Elem"
    setSleep = "set sleep"
    setScript = "set script"

class baseDataStructure:
    content = []

    def setContent(self,opration:opration,tag:str,**kwargs):
        """setContent

        Args:
            opration (opration): This args express what opration is. For example, select element.
            tag (str): This don't express what kind of html tag is. In this case this tag is used to identifiy actions which are defined by user.

        Note:
            To use this function you need to specify key and value at kwargs part.
            For example, Key="hello"
        """
        attributes = []
        for key,value in kwargs.items():
            Acontent = []
            Acontent .append(key)
            Acontent .append(value)
            attributes.append(Acontent)

        # [[a opration]]
        NextContent = [tag,opration,attributes]
        self.content.append(NextContent)





# class elemSelector(baseDataStructure):

#     # [tag,ID,value],[same thing], ...
#     def setContent(self,tag,ID,value):
#         temp = []
#         temp.append(tag)
#         temp.append(ID)
#         temp.append(value)
#         self.content.append(temp)



# class scriptData(baseDataStructure):

#     # [tag,stringOfScript],[same thing], ...
#     def setScript(self,tag,scriptString:str):
#         temp = []
#         temp.append(tag)
#         temp.append(scriptString)
#         self.content.append(temp)



# class waitTime(baseDataStructure):

#     # [tag,time(float)],[same thing], ...
#     def setTime(self,tag,time):
#         temp = []
#         temp.append(tag)
#         temp.append(float(time))
#         self.content.append(temp)