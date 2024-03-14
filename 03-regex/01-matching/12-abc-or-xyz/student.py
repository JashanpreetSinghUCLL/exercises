import re

def abc_or_xyz(string):
    return re.fullmatch("(abc)|(xyz)", string) is not None

print(abc_or_xyz("xer"))