n = int(input())
comma = ","
period = "."
underscore = "_"

for i in range(n):
    new_string = input()
    if comma in new_string or period in new_string or underscore in new_string:
        print(f"{new_string} is not pure!")
    else:
        print(f"{new_string} is pure.")
