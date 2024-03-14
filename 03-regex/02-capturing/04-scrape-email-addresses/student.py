import re

def scrape_email_addresses(string):
    return re.findall(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.]+', string)

text = """
Feel free to contact us at:

info@example.com
support@example.com

We'll be happy to assist you!
"""

print(scrape_email_addresses(text))
