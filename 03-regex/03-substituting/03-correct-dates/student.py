import re

def correct_dates(string):
    return re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\1/\3', string)

dates = "3/27/2034, 4/3/2023"
print(correct_dates(dates))

