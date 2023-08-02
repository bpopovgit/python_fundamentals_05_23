def change(new_string, command):
    char = command[1]
    replacement = command[2]
    new_string = new_string.replace(char, replacement)
    return new_string


def includes_or_not(new_string, command):
    substring = command[1]
    if substring in new_string:
        return True
    return False


def ends_or_not(new_string, command):
    substring = command[1]
    if new_string.endswith(substring):
        return True
    return False


def uppercase(new_string):
    new_string = new_string.upper()
    return new_string


def find_index(new_string, command):
    char = command[1]
    index_out = new_string.find(char)
    return index_out


def cut(new_string, command):
    start_index = int(command[1])
    count = int(command[2])
    out_string = new_string[start_index:start_index + count]
    return out_string


my_string = input()
current_command = input()
while current_command != "Done":
    current_command = current_command.split(" ")
    action = current_command[0]
    if action == "Change":
        my_string = change(my_string, current_command)
        print(my_string)
    elif action == "Includes":
        includes_check = includes_or_not(my_string, current_command)
        print(includes_check)
    elif action == "End":
        ends_check = ends_or_not(my_string, current_command)
        print(ends_check)
    elif action == "Uppercase":
        my_string = uppercase(my_string)
        print(my_string)
    elif action == "FindIndex":
        my_index = find_index(my_string, current_command)
        print(my_index)
    elif action == "Cut":
        my_string = cut(my_string, current_command)
        print(my_string)

    current_command = input()
