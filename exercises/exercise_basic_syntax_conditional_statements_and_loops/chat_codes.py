n = int(input())

for i in range(n):
    new_message = int(input())

    if new_message == 88:
        print("Hello")
    elif new_message == 86:
        print("How are you?")
    elif new_message < 88:
        print("GREAT!")
    elif new_message > 88:
        print("Bye.")