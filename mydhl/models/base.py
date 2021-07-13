
#==============[HELPER FUNCTIONS]=================#

def getIndexWithValue(list, attribute, value):

    for index, obj in enumerate(list):
        if hasattr(obj, attribute):
            if getattr(obj, attribute) == value:
                return index
    
    return None

def getObjectWithValue(list, attribute, value):

    for index, obj in enumerate(list):
        if hasattr(obj, attribute):
            if getattr(obj, attribute) == value:
                return obj
    
    return None


#==============[BASE MODELS]=================#

class BaseModel:

    def parse(self, json):
        for key, value in json.items():
            key = ''.join(e.lower() for e in key if e.isalnum())
            if hasattr(self, key): setattr(self, key, value)

        return self


class ObjectListModel(BaseModel):

    def __init__(self, list=[]):

        self.list = list

    def addToList(self, item):
        self.list.append(item)
        return self.list
    
    def removeFromList(self, item):
        self.list.remove(item)
        return self.list

    def getItemIndex(self, attribute, value):
        index = getIndexWithValue(self.list, attribute, value)
        return index
    
    def getItemObject(self, attribute, value):
        object = getObjectWithValue(self.list, attribute, value)
        return object