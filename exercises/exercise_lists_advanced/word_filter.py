words = input().split()
words_filter = [word for word in words if len(word) % 2 == 0]
print("\n".join(words_filter))
