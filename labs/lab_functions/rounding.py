def rounding(some_numbers):
    for num in given_numbers:
        rounded_nums.append(round(float(num)))
    return rounded_nums


given_numbers = input().split()
rounded_nums = []
print(rounding(given_numbers))
