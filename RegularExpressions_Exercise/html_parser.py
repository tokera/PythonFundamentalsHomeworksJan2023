import re


def remove_html(string):
    return regex.sub('', string)


html_text = input()

pattern = r"<title>(.*?)<\/title>|<body>(.*?)<\/body>"

title_and_body = re.findall(pattern, html_text)

raw_title = title_and_body[0][0]
raw_body = title_and_body[1][1]

regex = re.compile(r'<[^>]+>|\\n')

title = remove_html(raw_title)
body = remove_html(raw_body)

print(f"Title: {title}")
print(f"Content: {body}")
