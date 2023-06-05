def check_palindrome_num(my_nums):
    if my_nums == my_nums[::-1]:
        return True
    return False


positive_nums = input().split(", ")
# positive_nums_as_digits = []
# for num in positive_nums:
#     positive_nums_as_digits.append(int(num))
for number in positive_nums:
    print(check_palindrome_num(number))


