secret_message = input().split(" ")
deciphered = []

for word in secret_message:
    ascii_char = [char for char in word if char.isdigit()]
    words_list = [char for char in word if char not in ascii_char]

    first_letter = chr(int(''.join(ascii_char)))
    words_list[0], words_list[-1] = words_list[-1], words_list[0]
    new_word = first_letter + ''.join(words_list)
    deciphered.append(new_word)

print(' '.join(deciphered))