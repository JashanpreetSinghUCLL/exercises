import re

def only_letters(string):
    return re.fullmatch("[a-zA-Z]*", string) is not None

print(only_letters("Abcd"))
