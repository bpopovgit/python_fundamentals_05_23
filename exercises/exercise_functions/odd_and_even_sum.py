def summ_even_and_odd(num_elements):
    even_elements = []
    odd_elements = []
    for element in num_elements:
        if element % 2 == 0:
            even_elements.append(element)
        else:
            odd_elements.append(element)
    return sum(even_elements), sum(odd_elements)


def extract_num_summary(my_number):
    num_elements = [int(digit) for digit in str(my_number)]
    sum_even_elements, sum_odd_elements = summ_even_and_odd(num_elements)

    print(f"Odd sum = {sum_odd_elements}, Even sum = {sum_even_elements}")
    return sum_even_elements, sum_odd_elements


my_num = int(input())
sum_even_elements, sum_odd_elements = extract_num_summary(my_num)

# my_number = 1000435
# zz = [int(digit) for digit in str(my_number)]
