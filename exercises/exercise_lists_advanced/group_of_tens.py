sequence_of_numbers = [int(number) for number in input().split(", ")]
current_group_of_numbers = 10
while sequence_of_numbers:
    filtered_list_for_current_group = [number for number in sequence_of_numbers if number <= current_group_of_numbers]
    print(f"Group of {current_group_of_numbers}'s: {filtered_list_for_current_group}")
    current_group_of_numbers += 10
    sequence_of_numbers = [number for number in sequence_of_numbers if number not in filtered_list_for_current_group]


