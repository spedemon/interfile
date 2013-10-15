
class ParsingError(Exception): 
    def __init__(self,value):
        self.value = value 
    def __str__(self): 
        return "Parsing Error: "+repr(self.value)






