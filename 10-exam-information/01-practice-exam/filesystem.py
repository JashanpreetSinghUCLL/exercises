import re
from abc import ABC, abstractmethod


class StorageDevice:

    def __init__(self, block_count, block_size):
        self.__block_size = block_size
        self.__available_blocks = set(range(block_count))
        self.__used_blocks = set()

    @property
    def available_block_count(self):
        return len(self.__available_blocks)

    @property
    def used_block_count(self):
        return len(self.__used_blocks)

    @property
    def total_block_count(self):
        return len(list(self.__available_blocks.union(self.__used_blocks)))

    @property
    def block_size(self):
        return self.__block_size

    def allocate(self, block_count):
        if block_count > len(self.__available_blocks):
            raise RuntimeError("There are insufficient available blocks left")

        taken_blocks = []

        for _ in range(block_count):
            block = self.__available_blocks.pop()
            taken_blocks.append(block)
            self.__used_blocks.add(block)

        # print("Available blocks:",sorted( self.__available_blocks))
        # print("Used blocks:", sorted(self.__used_blocks))
        # print("Taken blocks:", taken_blocks)
        return taken_blocks

    def free(self, blocks):
        for block in blocks:
            if block in self.__used_blocks:
                self.__used_blocks.remove(block)
                self.__available_blocks.add(block)
            else:
                raise RuntimeError(f"{block} is not in used blocks")

        # print("Available blocks:", sorted(self.__available_blocks))
        # print("Used blocks:", sorted(self.__used_blocks))


# storage = StorageDevice(block_count=10, block_size=5)
# # print(storage.block_size)
# # print(storage.total_block_count)
# # print(storage.available_block_count)
# # print(storage.used_block_count)
# # print(storage.available_block_count)
# # print(storage.used_block_count)
# print(storage.allocate(5))
# storage.free([2, 3, 4])


# print(storage.available_block_count)
# print(storage.used_block_count)

class Entity(ABC):

    def __init__(self, storage, name):
        if not Entity.is_valid_name(name):
            raise RuntimeError("The given name is not valid")
        self.__storage = storage
        self.__name = name

    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r'[a-zA-Z0-9.]{1,16}$', name) is not None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not Entity.is_valid_name(new_name):
            raise RuntimeError("The given name is not valid")
        self.__name = new_name

    @property
    def storage(self):
        return self.__storage

    @property
    @abstractmethod
    def size_in_blocks(self):
        pass

    @property
    def size_in_bytes(self):
        return self.size_in_blocks * self.__storage.block_size

    @abstractmethod
    def clear(self):
        pass


class File(Entity):

    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__allocated_blocks = set()

    def grow(self, block_count):
        new_blocks = self.storage.allocate(block_count)
        self.__allocated_blocks.update(new_blocks)

    @property
    def size_in_blocks(self):
        return len(self.__allocated_blocks)

    def clear(self):
        self.storage.free(self.__allocated_blocks)
        self.__allocated_blocks.clear()


#
# my_ssd = StorageDevice(block_count=10, block_size=4096)
# file = File(storage=my_ssd, name='filename.txt')
# print(file.name)
#
# file.name = "newname.txt"
# print(file.name)
#
# # file.name = "invalid name"
# print(file.name)
#
# file.grow(block_count=8)
# print(file.size_in_blocks)
# print(my_ssd.available_block_count)
# print(file.size_in_bytes)
# file.clear()
# print(file.size_in_blocks)
# print(my_ssd.available_block_count)
# print(my_ssd.used_block_count)

class Directory(Entity):

    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__children = []

    def add(self, entity):
        self.__children.append(entity)

    @property
    def size_in_blocks(self):
        return sum(child.size_in_blocks for child in self.__children)

    def clear(self):
        for child in self.__children:
            child.clear()
        self.__children.clear()


my_ssd = StorageDevice(block_count=1000, block_size=4096)
directory = Directory(storage=my_ssd, name='myfolder')

print(directory.size_in_blocks)  # Expected: 0

file1 = File(my_ssd, 'file1')
file1.grow(5)
directory.add(file1)

print(directory.size_in_blocks)  # Expected: 5

file2 = File(my_ssd, 'file2')
file2.grow(10)
directory.add(file2)
print(directory.size_in_blocks)  # Expected: 15

subdir = Directory(my_ssd, 'subdir')
directory.add(subdir)
file3 = File(my_ssd, 'file3')
file3.grow(20)
subdir.add(file3)

print(directory.size_in_blocks)

directory.clear()
print(directory.size_in_blocks)
print(file1.size_in_blocks)
print(file2.size_in_blocks)
print(file3.size_in_blocks)
