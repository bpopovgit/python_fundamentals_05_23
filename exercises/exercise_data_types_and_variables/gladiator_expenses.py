lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
number_of_broken_helmets = lost_fights // 2
number_of_broken_swords = lost_fights // 3
number_of_broken_shields = lost_fights // 6
number_of_broken_armor = number_of_broken_shields // 2
total_expenses = number_of_broken_helmets * helmet_price\
                 + number_of_broken_swords * sword_price\
                 + number_of_broken_shields * shield_price\
                 + number_of_broken_armor * armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
