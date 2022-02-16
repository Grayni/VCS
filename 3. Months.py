# months

# [1] List
lst = [
    ['winter', [12, 1, 2]],
    ['spring', [3, 4, 5]],
    ['summer', [6, 7, 8]],
    ['autumn', [9, 10, 11]]
]

month_user = int(input('Enter month: '))

for season in lst:
    if month_user in season[1]:
        print(f'[1] Season - {season[0]}')

# [2] Dict

obj = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}

# Get "month_user" in [1] List.
for season in obj:
    if month_user in obj[season]:
        print(f'[2] Season - {season}')
