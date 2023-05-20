while True:
    command = input()
    new_string = ""
    if command == "End":
        break
    elif command == "SoftUni":
        continue
    for character in command:
        new_string += character * 2
    print(new_string)

