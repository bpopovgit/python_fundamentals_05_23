import re

sentence = input()
searched_for_word = input()
pattern = fr"\b{searched_for_word}\b"
matches = re.findall(pattern, sentence, re.IGNORECASE)
print(len(matches))