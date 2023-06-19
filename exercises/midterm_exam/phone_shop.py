def add_phone(phones, phone_input):
    if phone_input not in phones:
        phones.append(phone_input)
    return phones


def remove_phone(phones, phone_input):
    if phone_input in phones:
        phones.remove(phone_input)
    return phones


def add_bonus_phone(phones, phone_input):
    phone_input_list = phone_input.split(":")
    input_old, input_new = phone_input_list[0], phone_input_list[1]
    if input_old in phones:
        index_old = phones.index(input_old)
        phones.insert(index_old + 1, input_new)

    return phones


def update_last_phone(phones, phone_input):
    if phone_input in phones:
        phones.remove(phone_input)
        phones.append(phone_input)
    return phones


list_of_phones = input().split(", ")
command = input()

while command != "End":
    command = command.split()
    action = command[0]
    if action == "Add":
        phone = command[2]
        list_of_phones = add_phone(list_of_phones, phone)
    elif action == "Remove":
        phone = command[2]
        list_of_phones = remove_phone(list_of_phones, phone)
    elif action == "Bonus":
        phone = command[3]
        list_of_phones = add_bonus_phone(list_of_phones, phone)
    elif action == "Last":
        phone = command[2]
        list_of_phones = update_last_phone(list_of_phones, phone)
    command = input()

print(", ".join(list_of_phones))


