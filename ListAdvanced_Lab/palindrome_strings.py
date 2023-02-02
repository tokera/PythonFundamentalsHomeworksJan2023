strings = input().split()
palindrome = input()

# first solution
#palindromes = [w for w in strings if w == w[::-1]]

# second solution
palindromes = [w for w in strings if w == "".join(reversed(w))]

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")
