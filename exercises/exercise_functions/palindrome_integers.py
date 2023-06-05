def check_palindrome_num(my_nums):
    if my_nums == my_nums[::-1]:
        return True
    return False


def get_palindrome_output(input_nums):
    input_integers = input_nums.split(", ")
    for input_int in input_integers:
        print(check_palindrome_num(input_int))


positive_nums = input()


get_palindrome_output(positive_nums)
