n = int(input())

for i in range(n):
    new_number = int(input())

    if new_number % 2 != 0:
        print(f"{new_number} is odd!")
        break

if new_number % 2 == 0:
    print("All numbers are even.")
