import re

def one_or_more_b(string):
    return re.fullmatch("b+", string) is not None





































# def one_or_more_b(string):
#     pattern = re.compile(r'.*b+.*')
#     return re.fullmatch(pattern, string)

# print(one_or_more_b("bbba"))
