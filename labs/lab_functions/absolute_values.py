def absolute_value():
    for num in num_sequence:
        abs_list.append(abs(float(num)))
    return abs_list


num_sequence = input().split()
abs_list = []
print(absolute_value())

