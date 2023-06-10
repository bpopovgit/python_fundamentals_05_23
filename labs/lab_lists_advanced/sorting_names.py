def sort_names():
    names_list = input().split(", ")
    sorted_list = sorted(names_list, key=lambda x: (-len(x), x))
    return sorted_list


print(sort_names())
