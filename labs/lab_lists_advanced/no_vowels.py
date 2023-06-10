text = input()
letters = [letter for letter in text if letter.lower() not in ('a', 'e', 'o', 'u', 'i')]
print("".join(letters))