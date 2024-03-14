import re

def equals_b(string):
    return re.fullmatch("b", string)

print(equals_b("b"))