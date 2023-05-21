number_of_snowballs = int(input())
highest_snowball_value = 0
highest_snowball_weight = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed_to_hit_target = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight/time_needed_to_hit_target) ** snowball_quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        highest_snowball_weight = snowball_weight
        highest_snowball_time = time_needed_to_hit_target
        highest_snowball_quality = snowball_quality

print(f"{highest_snowball_weight} : {highest_snowball_time} = {int(highest_snowball_value)} ({highest_snowball_quality})")

