def check_palindrome_word(word):
    if word == word[::-1]:
        return word


words = input().split()
searched_for_word = input()

palindrome_list = [word for word in words if check_palindrome_word(word)]
palindrome_counter = palindrome_list.count(searched_for_word)

print(f"{palindrome_list}")
print(f"Found palindrome {palindrome_counter} times")

