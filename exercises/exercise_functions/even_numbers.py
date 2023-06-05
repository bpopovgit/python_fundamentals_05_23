def print_only_even_numbers(sequence):
    integer_items = [int(i) for i in sequence.split()]
    even_output = [i for i in integer_items if i % 2 == 0]
    return even_output

my_sequence = input()
print(print_only_even_numbers(my_sequence))
