# def sort_sequence(sequence):
#     my_list = sorted([int(i) for i in sequence.split()])
#     return my_list
#
#
# my_sequence = input()
# print(sort_sequence(my_sequence))

def is_even(number):
    if number % 2 == 0:
        return number


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))

result = list(filter(is_even, numbers_as_digits))
print(result)
