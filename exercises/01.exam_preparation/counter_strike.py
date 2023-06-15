energy = int(input())
distance = input()
battles_won = 0

while distance != "End of battle":
    distance_in_int = int(distance)

    if energy >= distance_in_int:
        battles_won += 1
        energy -= distance_in_int
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        break

    distance = input()

else:
    print(f"Won battles: {battles_won}. Energy left: {energy}")
