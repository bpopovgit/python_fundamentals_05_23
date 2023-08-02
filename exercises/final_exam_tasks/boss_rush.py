import re

number_of_bosses = int(input())
pattern = r"(\|)([A-Z]{4,})\1:(#)([A-Za-z]+ [A-Za-z]+)\3"
for boss in range(number_of_bosses):
    new_boss = input()
    matches = re.findall(pattern, new_boss)
    if matches:
        strength = len(matches[0][1])
        armor = len(matches[0][3])
        print(f"{matches[0][1]}, The {matches[0][3]}")
        print(f">> Strength: {strength}")
        print(f">> Armor: {armor}")
    else:
        print("Access denied!")
