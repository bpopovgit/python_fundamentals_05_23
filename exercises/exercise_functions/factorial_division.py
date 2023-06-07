def calculate_factorial(number_one, number_two):
    for current_number_one in range(1, number_one):
        number_one *= current_number_one
    for current_number_two in range(1, number_two):
        number_two *= current_number_two
    division_result = number_one / number_two
    return f"{division_result:.2f}"


# def divide_factorial_result(first_num, second_num):
#     calculate_factorial(divmod(first_num, second_num))


first_number = int(input())
second_number = int(input())
print(calculate_factorial(first_number, second_number))
