MAX_SIZE = 4
people = int(input())
lift = [int(x) for x in input().split()]

for i in range(len(lift)):
    free_space = MAX_SIZE - lift[i]

    if people >= free_space:
        lift[i] += free_space
    else:
        lift[i] += people

    people -= free_space

    if people <= 0 and (i != len(lift) - 1 or lift[i] < MAX_SIZE):
        print(f"The lift has empty spots!")
        break
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(*lift)