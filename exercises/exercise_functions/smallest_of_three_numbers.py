def smallest_of_three(first, second, third):
    all_elements = sorted([first, second, third])
    return all_elements[0]


num_one = int(input())
num_two = int(input())
num_three = int(input())
print(smallest_of_three(num_one, num_two, num_three))
