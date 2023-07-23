import re
dates = input()
regex = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
# matches = re.findall(regex, dates)
matches = re.finditer(regex, dates)

for match in matches:
    day = match.group(1)
    separator = match.group(2)
    month = match.group(3)
    year = match.group(4)
    #below is used with re.findall
    # day = match[0]
    # separator = match[1]
    # month = match[2]
    # year = match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')
