def add_animal(animal_dict, command):
    animal_name, needed_food_quantity, area = command[1].split("-")
    if animal_name not in animal_dict:
        animal_dict[animal_name] = {"needed_food_quantity": int(needed_food_quantity), "area": area}
    else:
        animal_dict[animal_name]["needed_food_quantity"] += int(needed_food_quantity)
    return animal_dict



def feed_animal(animal_dict, command):
    animal_name, food = command[1].split("-")

    if animal_name in animal_dict:
        animal_dict[animal_name]["needed_food_quantity"] -= int(food)
        if animal_dict[animal_name]["needed_food_quantity"] <= 0:
            del animal_dict[animal_name]
            print(f"{animal_name} was successfully fed")
    return animal_dict



animal_information = {}
current_command = input()
while current_command != "EndDay":
    current_command = current_command.split()
    action = current_command[0]
    if action == "Add:":
        animal_information = add_animal(animal_information, current_command)
        # print(animal_information)
    elif action == "Feed:":
        animal_information = feed_animal(animal_information, current_command)

    current_command = input()

hungry_animals = {}
for animal_name in animal_information.keys():
    current_area = animal_information[animal_name]["area"]
    if current_area not in hungry_animals:
        hungry_value = 1 if int(animal_information[animal_name]["needed_food_quantity"]) > 0 else 0
        hungry_animals[current_area] = hungry_value
    else:
        hungry_value = 1 if int(animal_information[animal_name]["needed_food_quantity"]) > 0 else 0
        hungry_animals[current_area] += hungry_value

print("Animals:")
for animal, needed_food_quantity in animal_information.items():
    food_quantity = animal_information[animal]["needed_food_quantity"]
    print(f" {animal} -> {food_quantity}g")
print("Areas with hungry animals:")

for i in hungry_animals:
    print(f"{i}: {hungry_animals[i]}")

