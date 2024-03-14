import re

def remove_trailing_whitespace(string):
    return re.sub(r"\s+$", "", string, flags=re.MULTILINE)


text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed       blandit magna vel mi varius, nec dapibus orci suscipit.
Quisque ac      lectus vitae mauris varius laoreet.
Vestibulum nec est quis elit finibus luctus.
Nulla facilisi. Ut euismod quam eget velit dignissim, vel posuere nisi sollicitudin. 
Sed rutrum interdum ligula, at ultricies purus varius nec. In hac habitasse platea dictumst.
"""
print(remove_trailing_whitespace(text))