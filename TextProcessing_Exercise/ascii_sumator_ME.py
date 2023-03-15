first_symbol = input()
second_symbol = input()
symbols = input()

first_symbol_ascii_val = ord(first_symbol)
second_symbol_ascii_val = ord(second_symbol)

range_of_symbols = sorted([first_symbol_ascii_val, second_symbol_ascii_val])
sum_of_char_in_range = 0

for ch in symbols:
    ch_ascii_val = ord(ch)
    if range_of_symbols[0] < ch_ascii_val < range_of_symbols[1]:
        sum_of_char_in_range += ch_ascii_val

print(sum_of_char_in_range)
