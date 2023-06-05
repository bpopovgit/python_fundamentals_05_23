def get_chars_in_range(character_one, character_two):
    output = []
    for num in range(ord(character_one) + 1, ord(character_two)):
        output.append(chr(num))
    return " ".join(output)


char_one = input()
char_two = input()
print(get_chars_in_range(char_one, char_two))

#
#
# test = " ".join(['tra', 'lala'])
# ascii_items = ord('a')
