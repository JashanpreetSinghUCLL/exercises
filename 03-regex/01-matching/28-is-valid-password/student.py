import re

def is_valid_password(string):
    postive = [
        r".{12,}",
        r"\d",
        r"[a-z]",
        r"[A-Z]",
        r"[+-/.@*]"
    ]

    negative = [
        r"(.)\1{2}",
        r"(.)(.*\1){3}"
    ]

    for regex in postive:
        if not re.search(regex, string):
            return False
        
    for regex in negative:
        if re.search(regex, string):
            return False
    
    return True