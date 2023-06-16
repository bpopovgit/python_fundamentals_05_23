employee_one_efficiency = int(input())
employee_two_efficiency = int(input())
employee_three_efficiency = int(input())
students_count = int(input())
total_employee_efficiency = employee_one_efficiency + employee_two_efficiency + employee_three_efficiency
hours_counter = 0
total_time = 0

while students_count >= 0:
    hours_counter += 1
    total_time += 1
    if hours_counter % 4 == 0:
        continue

    students_count -= total_employee_efficiency

print(f"Time needed: {total_time}h.")
