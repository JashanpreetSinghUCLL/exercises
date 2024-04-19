from operator import attrgetter

def sort_by_age(people):
    return sorted(people, key=attrgetter('age'))

def sort_by_decreasing_age(people):
    return sorted(people, key=attrgetter('age'), reverse=True)

def sort_by_name(people):
    return sorted(people, key=lambda person: person.name)

def sort_by_name_then_age(people):
    return sorted(people, key=lambda person: (person.name, person.age))

def sort_by_name_then_decreasing_age(people):
    return sorted(people, key=lambda person: (person.name, -person.age))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_name(self):
        return self.name
    

    @property
    def get_age(self):
        return self.age
    

    def __repr__(self):
        return f'{self.name}, {self.age})'

people = [Person("Jashan", 20), Person("John", 30), Person("Hazel", 12)]

sorted_people = sort_by_name(people)
print(sorted_people)