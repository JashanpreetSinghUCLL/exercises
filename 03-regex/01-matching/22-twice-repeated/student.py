import re

def twice_repeated(string):
    return re.fullmatch(r"(.+)\1", string) is not None

print(twice_repeated("55"))