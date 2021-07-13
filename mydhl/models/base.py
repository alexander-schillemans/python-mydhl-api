
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

            if hasattr(self, key): 
                attrVal = getattr(self, key)

                if isinstance(attrVal, BaseModel):
                    setattr(self, key, attrVal.parse(value))
                else:
                    setattr(self, key, value)

        return self


class ObjectListModel(BaseModel):

    def __init__(self, list=[], listObject=None):

        self.list = list
        self.listObject = listObject

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
    
    def parse(self, json):

        if isinstance(json, dict):
            itemObj = self.listObject().parse(json)
            self.addToList(itemObj)
        elif isinstance(json, list):
            for item in json:
                itemObj = self.listObject().parse(item)
                self.addToList(itemObj)

        return self