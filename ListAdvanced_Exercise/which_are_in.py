first_sequence = input().split(", ")
second_sequence = input().split(", ")

new_sequence_with_duplicates = [x for x in first_sequence for y in second_sequence if x in y]

# seen = set()
# seen_add = seen.add
# unique_seq = [x for x in new_sequence_with_duplicates if not (x in seen or seen_add(x))]
result_sequence = sorted(set(new_sequence_with_duplicates), key=new_sequence_with_duplicates.index)
#result_sequence = []

# for f_str in first_sequence:
#     adding_el = False
#     for s_str in second_sequence:
#         if f_str in s_str:
#             adding_el = True
#     if adding_el:
#         result_sequence.append(f_str)

# for f_str in first_sequence:
#     is_contains = [x for x in second_sequence if f_str in x]
#     if is_contains:
#         result_sequence.append(f_str)

print(result_sequence)
