def grade_in_words(new_grade):
    if 2.00 <= grade_data <= 2.99:
        value = 'Fail'
    elif 3.00 <= grade_data <= 3.49:
        value = 'Poor'
    elif 3.50 <= grade_data <= 4.49:
        value = 'Good'
    elif 4.50 <= grade_data <= 5.49:
        value = 'Very Good'
    elif 5.50 <= grade_data <= 6.00:
        value = 'Excellent'
    return value


grade_data = float(input())
print(grade_in_words(grade_data))
