# def sum_numbers(num_one, num_two):
#     result = num_one + num_two
#     return result
#
#
# def subtract(summed, num_three):
#     result = summed - num_three
#     return result
#
#
# def add_and_subtract(num_one, num_two, num_three):
#     summed = sum_numbers(num_one, num_two)
#     result = subtract(summed, num_three)
#     return result

def add_and_subtract(num_one, num_two, num_three):
    def sum_numbers():
        summed_nums = num_one + num_two
        return summed_nums

    def subtract(summed_nums):
        subtracted_num = summed_nums - num_three
        return subtracted_num

    summed = sum_numbers()
    result = subtract(summed)

    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
