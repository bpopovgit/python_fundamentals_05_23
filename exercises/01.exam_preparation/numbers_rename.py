FIRST_COUNT = 5
integers_sequence = [int(x) for x in input().split()]
avg_result = sum(integers_sequence) / len(integers_sequence)
sorted_nums = sorted([x for x in integers_sequence if x > avg_result])
# sorted_nums = filter(lambda x: x > avg_result, integers_sequence)

if not sorted_nums:
    print("No")
else:
    print(*[sorted_nums.pop() for i in range(FIRST_COUNT) if sorted_nums])