import re

def collect_links(string):
    return re.findall(r'<a href="(.*)">', string)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic HTML with Links</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a basic HTML document with some links.</p>

    <h2>Links:</h2>
    <ul>
        <li><a href="https://www.example.com">Example Website</a></li>
        <li><a href="https://www.google.com">Google</a></li>
        <li><a href="https://www.wikipedia.org">Wikipedia</a></li>
    </ul>

    <p>Feel free to explore!</p>
</body>
</html>
"""

print(collect_links(html))