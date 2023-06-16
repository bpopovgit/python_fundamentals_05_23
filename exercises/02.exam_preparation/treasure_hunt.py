def loot(list_of_loot, list_of_items):
    for item in list_of_items:
        if item not in list_of_loot:
            list_of_loot.insert(0, item)
    return list_of_loot


def drop(list_of_loot, loot_index):
    if loot_index in range(len(list_of_loot)):
        removed_loot = list_of_loot.pop(loot_index)
        list_of_loot.insert(len(list_of_loot), removed_loot)
    return list_of_loot


def steal(list_of_loot, stolen_items_count):
    if stolen_items_count >= len(list_of_loot):
        print(", ".join(list_of_loot))
        list_of_loot = []
    else:
        steal_index = len(list_of_loot) - stolen_items_count
        print(", ".join(list_of_loot[steal_index:]))
        list_of_loot = list_of_loot[0:steal_index]
    return list_of_loot


initial_loot = input().split("|")
command = input()
while command != "Yohoho!":
    command = command.split()
    action = command[0]
    if action == "Loot":
        items = command[1:]
        initial_loot = loot(initial_loot, items)
    elif action == "Drop":
        index = int(command[1])
        initial_loot = drop(initial_loot, index)
    elif action == "Steal":
        count = int(command[1])
        initial_loot = steal(initial_loot, count)
    command = input()

if len(initial_loot) == 0:
    print(f"Failed treasure hunt.")
else:
    average_treasure_gain = sum(len(item) for item in initial_loot) / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
