import re

def parse_link(string):
    wellFormed = re.fullmatch(r'<a href="(.*)">(.*)</a>', string)

    if wellFormed:
        link, caption = wellFormed.groups()
        return (caption, link)
    else:
        return None
    
print(parse_link('<a href=\"jashan.com\">Jashan</a>'))
