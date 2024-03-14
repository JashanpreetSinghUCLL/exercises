import re

def only_digits(string):
    return re.fullmatch(r"\d*", string) is not None

print(only_digits("12a"))
