def cast_spell(heroes_dict, split_command):
    current_hero_name = split_command[1]
    mana_point_needed = int(split_command[2])
    spell_name = split_command[3]
    if heroes_dict[current_hero_name]["MANA_POINTS"] >= mana_point_needed:
        heroes_dict[current_hero_name]["MANA_POINTS"] -= mana_point_needed
        print(f"{current_hero_name} has successfully cast {spell_name}"
              f" and now has {heroes_dict[current_hero_name]['MANA_POINTS']} MP!")
    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")

    return heroes_dict


def take_damage(heroes_dict, split_command):
    current_hero_name = split_command[1]
    damage = int(split_command[2])
    attacker = split_command[3]
    heroes_dict[current_hero_name]["HIT_POINTS"] -= damage
    if heroes_dict[current_hero_name]["HIT_POINTS"] > 0:
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} and"
              f" now has {heroes_dict[current_hero_name]['HIT_POINTS']} HP left!")
    else:
        print(f"{current_hero_name} has been killed by {attacker}!")
        del heroes_dict[current_hero_name]
    return heroes_dict


def recharge(heroes_dict, split_command):
    current_hero_name = split_command[1]
    amount = int(split_command[2])
    recharged_amount = amount
    heroes_dict[current_hero_name]['MANA_POINTS'] += amount
    if heroes_dict[current_hero_name]['MANA_POINTS'] > 200:
        recharged_amount = amount - (heroes_dict[current_hero_name]['MANA_POINTS'] - 200)
        heroes_dict[current_hero_name]['MANA_POINTS'] = 200
    print(f"{current_hero_name} recharged for {recharged_amount} MP!")
    return heroes_dict


def heal(heroes_dict, split_command):
    current_hero_name = split_command[1]
    amount = int(split_command[2])
    healed_amount = amount
    heroes_dict[current_hero_name]['HIT_POINTS'] += amount
    if heroes_dict[current_hero_name]['HIT_POINTS'] > 100:
        healed_amount = amount - (heroes_dict[current_hero_name]['HIT_POINTS'] - 100)
        heroes_dict[current_hero_name]['HIT_POINTS'] = 100
    print(f"{current_hero_name} healed for {healed_amount} HP!")
    return heroes_dict


heroes = {}
number_of_heroes = int(input())
for hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"HIT_POINTS": int(hit_points), "MANA_POINTS": int(mana_points)}

command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        heroes = cast_spell(heroes, command)
    elif action == "TakeDamage":
        heroes = take_damage(heroes, command)
    elif action == "Recharge":
        heroes = recharge(heroes, command)
    elif action == "Heal":
        heroes = heal(heroes, command)

    command = input()

for hero_name, values in heroes.items():
    print(hero_name)
    print(f"HP: {values['HIT_POINTS']}")
    print(f"MP: {values['MANA_POINTS']}")