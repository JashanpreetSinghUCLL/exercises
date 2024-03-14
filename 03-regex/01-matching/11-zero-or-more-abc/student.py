import re

def zero_or_more_abc(string):
    return re.fullmatch("(abc)*", string) is not None

print(zero_or_more_abc(""))