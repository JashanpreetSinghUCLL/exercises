import re

def one_or_more_a(string):
    pattern = re.compile(r'a+')
    return re.fullmatch(pattern, string) is not None

print(one_or_more_a("aaabbbb"))