number_of_lines = int(input())
capacity = 255
total_liters_poured = 0
for i in range(number_of_lines):
    liters_of_water = int(input())
    total_liters_poured += liters_of_water
    if capacity < total_liters_poured:
        print("Insufficient capacity!")
        total_liters_poured -= liters_of_water
        continue

print(total_liters_poured)