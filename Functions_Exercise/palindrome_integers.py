numbers = list(map(int, input().split(", ")))


def check_for_palindromes(nums):

    for n in nums:
        num_to_str = str(n)
        if num_to_str == num_to_str[::-1]:
            print(True)
        else:
            print(False)


check_for_palindromes(numbers)
