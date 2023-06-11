def check_office_rooms(number_of_rooms):
    free_chairs = 0
    needed_chairs = 0
    for room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
            needed_chairs += abs(difference)
        else:
            free_chairs += difference

    return free_chairs, needed_chairs


number_of_rooms_in_business_center = int(input())
total_free_chairs, total_needed_chairs = check_office_rooms(number_of_rooms_in_business_center)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
