from Item import elemSelector,scriptData,waitTime

class oprationMaker:
    def __init__(self) -> None:
        pass


class indexMaker:
    def __init__(self) -> None:
        pass


class order:
    # Manage order by tag name.
    def __init__(self) -> None:
        self.NotRegistered = []
        self.Registered = []
        self.indexByTagName = []

    def NotRegisteredTag(self,tagName):
        self.NotRegistered.append(tagName)

    def registerTag(self,tagName):
        self.Registered.append(tagName)
        self.indexByTagName.append(tagName)