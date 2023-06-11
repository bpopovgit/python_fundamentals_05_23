numbers = [int(number) for number in input().split(", ")]
positive_numbers = [number for number in numbers if number >= 0]
negative_numbers = [number for number in numbers if number < 0]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]
print(f"Positive: {', '.join(str(number) for number in positive_numbers)}")
print(f"Negative: {', '.join(str(number) for number in negative_numbers)}")
print(f"Even: {', '.join(str(number) for number in even_numbers)}")
print(f"Odd: {', '.join(str(number) for number in odd_numbers)}")

