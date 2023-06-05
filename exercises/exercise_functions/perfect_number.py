def check_perfect_number(number):
    divisors_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


some_number = int(input())
print(check_perfect_number(some_number))
