string_input = input()
n = int(input())

repeat_string = lambda txt, count: txt * count

print(repeat_string(string_input, n))
