class CircularBuffer:
    
    def __init__(self, n):
        self.__max_size = n
        self.items = []

    def add(self, item):
        if len(self.items) >= self.__max_size:
            self.items.pop(0)
            self.items.append(item)
        else:
            self.items.append(item)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __len__(self):
        return len(self.items)
    

buffer = CircularBuffer(5)
print(buffer.__len__())
buffer.add("a")
buffer.add("b")
buffer.add("c")
buffer.add("e")
buffer.add("f")
buffer.add("g")
print(buffer.__len__())
print(buffer.__getitem__(0))
print(buffer.items)
