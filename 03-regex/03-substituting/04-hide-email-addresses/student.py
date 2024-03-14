import re

def hide_email_addresses(string):
    def replace(match):
        return '*' * len(match.group())
    
    return re.sub(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+', replace, string, flags=re.MULTILINE)

text = "Jashan@ucll.be, hello@fresh.be"
print(text)
print(hide_email_addresses(text))