def create_loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percentage = some_number // 10
    return f"{some_number}% [{'%' * loaded_percentage}{'.' * (10 - loaded_percentage)}]\nStill loading..."


# 30% [%%%.......]
# Still loading...

number = int(input())
print(create_loading_bar(number))
