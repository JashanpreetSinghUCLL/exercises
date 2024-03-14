import re

def is_valid_student_id(string):
    return re.fullmatch(r"(s|r|S|R)\d{7}+", string) is not None

print(is_valid_student_id("s12345623"))