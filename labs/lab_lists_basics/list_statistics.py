n = int(input())
positives = []
negatives = []
positives_count = 0
negatives_sum = 0
for number in range(n):
    new_num = int(input())
    if new_num >= 0:
        positives.append(new_num)
        positives_count += 1
    elif new_num < 0:
        negatives.append(new_num)
        negatives_sum += new_num

print(positives)
print(negatives)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {negatives_sum}")