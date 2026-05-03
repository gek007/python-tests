# write function :

# HTML Elements

# Have the function HTMLElements(str) read the str parameter being passed which will be a string of HTML DOM elements and plain text. The elements that will be used are: b, i, em, div, p. For example: if str is "<div><b><p>hello world</p></b></div>" then this string of DOM elements is nested correctly so your program should return the string true.

# If a string is not nested correctly, return the first element encountered where, if changed into a different element, would result in a properly formatted string. If the string is not formatted properly, then it will only be one element that needs to be changed. For example: if str is "<div><i>hello</i>world</b>" then your program should return the string div because if the first <div> element were changed into a <b>, the string would be properly formatted.

# Examples

# Input: "<div><div><b></b></div></p>"
# Output: div

# Input: "<div>abc</div><p><em><i>test test test</b></em></p>"
# Output: i


import re


def HTMLElements(str):
    # Find all tags that are opening or closing tags for b, i, em, div, or p.
    # The regex captures tags like <b>, </i>, <div>, etc., but ignores other tags or text.
    tags = re.findall(r"</?(?:b|i|em|div|p)>", str)
    stack = []

    for tag in tags:
        is_closing = tag.startswith("</")
        print(is_closing)
        element = tag[2:-1] if is_closing else tag[1:-1]

        if is_closing:
            if stack and stack[-1] == element:
                stack.pop()
            else:
                return stack[-1] if stack else element
        else:
            stack.append(element)

    return "true" if not stack else stack[-1]


print(HTMLElements("<div><b><p>hello world</p></b></div>"))  # true
print(HTMLElements("<div><i>hello</i>world</b>"))  # div
print(HTMLElements("<div><div><b></b></div></p>"))  # div
print(HTMLElements("<div>abc</div><p><em><i>test test test</b></em></p>"))  # i
