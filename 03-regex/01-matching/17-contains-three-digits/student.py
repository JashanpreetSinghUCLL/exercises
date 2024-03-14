import re

def contains_three_digits(string):
    return len(re.findall(r"\d", string)) >= 3

print(contains_three_digits("1 2 3adzde3"))