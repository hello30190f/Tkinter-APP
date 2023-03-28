class baseDataStructure:
    content = []

    def setContent(self,opration:str,tag:str,**kwargs):
        """setContent

        Args:
            opration (str): _description_
            tag (str): _description_

        Note:
            To use this function you need to specify key and value at kwargs arg part.
            Key="hello"
        """
        for key,value in kwargs.items():
            Acontent = []
            attrribute = []
            attrribute.append(key)
            attrribute.append(value)
            Acontent.append(opration)
            Acontent.append(tag)
            Acontent.append(attrribute)



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