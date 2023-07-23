strings_sequence = input().split(" ")
final_string = [text * len(text) for text in strings_sequence]

print(''.join(final_string))