number_of_coffees_needed = 0

while True:
    command = input()
    if command == "END":
        if number_of_coffees_needed > 5:
            print("You need extra sleep")
        else:
            print(number_of_coffees_needed)
        break
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.islower():
            number_of_coffees_needed += 1
        elif command.isupper():
            number_of_coffees_needed += 2
    else:
        continue

