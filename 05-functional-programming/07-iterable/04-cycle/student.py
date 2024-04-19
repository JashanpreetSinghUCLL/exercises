

class Cycle:

    def __init__(self, elements):
        self.__elements = list(elements)
        self.__index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index = (self.__index + 1) % len(self.__elements)
        return self.__elements[self.__index]
    
