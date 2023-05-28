n = int(input())
word = input()
my_list_one = []

for string in range(n):
    new_string = input()
    my_list_one.append(new_string)

print(my_list_one)

for i in range(len(my_list_one) - 1, -1, -1):
    element = my_list_one[i]
    if word not in element:
        my_list_one.remove(element)
print(my_list_one)
