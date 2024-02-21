class Queue:
    def __init__(self):
        self.__queue = []
    
    def add(self, item):
        self.__queue.append(item)
    
    def next(self):
        for i in range(0, 2):
            first_served = self.__queue[i]
            self.__queue.pop(i)
            return first_served
    
    def is_empty(self):
        return len(self.__queue) == 0
    
queue = Queue()
queue.add("Alice")
queue.add("Bob")
queue.add("Lewis")
queue.add("Matt")

print(queue.next())
print(queue.next())


