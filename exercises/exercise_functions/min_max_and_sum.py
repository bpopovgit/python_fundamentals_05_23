def min_num(sequence: list):
    my_min_num = min(sequence)
    return f"The minimum number is {my_min_num}"


def max_num(sequence: list):
    my_max_num = max(sequence)
    return f"The maximum number is {my_max_num}"


def sum_numbers(sequence: list):
    sum_of_nums = sum(sequence)
    return f"The sum number is: {sum_of_nums}"


my_sequence = input().split()
my_sequence_digits = []
for num in my_sequence:
    my_sequence_digits.append(int(num))

print(min_num(my_sequence_digits))
print(max_num(my_sequence_digits))
print(sum_numbers(my_sequence_digits))
