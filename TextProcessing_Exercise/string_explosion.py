text = input()

exploded_mark_found = False
result = ""
remainder = 0
count_of_symbols_to_remove = 0

for ch in text:
    if exploded_mark_found:
        count_of_symbols_to_remove = int(ch) + remainder
        exploded_mark_found = False
        remainder = 0

    if count_of_symbols_to_remove > 0:
        if ch == ">":
            remainder = count_of_symbols_to_remove
            count_of_symbols_to_remove = 0
        else:
            count_of_symbols_to_remove -= 1
            continue

    if ch == ">":
        exploded_mark_found = True
        result += ch
    else:
        result += ch

print(result)
