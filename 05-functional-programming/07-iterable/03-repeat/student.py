

class Repeat:

    def __init__(self, element):
        self.__element = element

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.__element
    
xs = Repeat(5)

print(next(xs))