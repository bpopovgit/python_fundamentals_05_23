phonebook = {}

while True:
    info = input()
    if "-" not in info:
        break
    name, phone_number = info.split("-")
    phonebook[name] = phone_number

for search in range(int(info)):
    searched_for_name = input()
    if searched_for_name in phonebook.keys():
        print(f"{searched_for_name} -> {phonebook[searched_for_name]}")
    else:
        print(f"Contact {searched_for_name} does not exist.")