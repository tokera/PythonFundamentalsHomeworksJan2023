import re

number_of_barcodes = int(input())

pattern_for_match_barcodes = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
pattern_fot_match_digits = r"[0-9]"

for _ in range(number_of_barcodes):
    barcode = input()

    matching_barcodes = re.findall(pattern_for_match_barcodes, barcode)
    if not matching_barcodes:
        print("Invalid barcode")
        continue

    matching_digits = re.findall(pattern_fot_match_digits, matching_barcodes[0][1])
    group = "00"

    if matching_digits:
        group = ""
        for d in matching_digits:
            group += d

    print(f"Product group: {group}")
