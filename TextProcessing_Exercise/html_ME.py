def print_structure_of_html(content_to_print, tag):
    print(f"<{tag}>")
    print(f"    {content_to_print}")
    print(f"</{tag}>")


title = input()
content = input()
print_structure_of_html(title, "h1")
print_structure_of_html(content, "article")

comment = input()
while comment != "end of comments":
    print_structure_of_html(comment, "div")

    comment = input()
