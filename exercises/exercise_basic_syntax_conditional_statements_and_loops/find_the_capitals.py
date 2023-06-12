def find_capital_letters(word):
    capital_letters = []
    for index, char in enumerate(word):
        if char.isupper():
            capital_letters.append(index)
    return capital_letters


my_word = input()
print(find_capital_letters(my_word))