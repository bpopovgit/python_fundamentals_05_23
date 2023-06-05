def calculations(operator_a, num_one_a: int, num_two_a: int):
    if operator == "add":
        result = num_one + num_two
    elif operator == "subtract":
        result = num_one - num_two
    elif operator == "multiply":
        result = num_one * num_two
    elif operator == "divide":
        result = num_one // num_two
    return result


operator = input()
num_one = int(input())
num_two = int(input())
print(calculations(operator, num_one, num_two))
