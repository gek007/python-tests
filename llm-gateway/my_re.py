import re

text = "The price is 42 dollars"

# Search anywhere
match = re.search(r"\d+", text)
if match:
    print(match.group())      # Output: 42
    print(match.span())       # Output: (13, 15)