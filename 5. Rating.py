# Structure "Rating"
my_list = [7, 5, 3, 3, 2]
num = int(input('Enter number: '))

for i, mark in enumerate(my_list):
    if num >= mark:
        my_list.insert(i, num)
        break
    elif num < my_list[-1]:
        my_list.append(num)
        break

print(my_list)


# Complex solution
print()
print('-- COMPLEX SOLUTION --', end='\n\n')
print('Create new rating.')
# create Rating
my_rating = input('Enter several values separated by a space: ')
my_rating = sorted(list(map(int, my_rating.split())), reverse=True)
print(f'Your table of rating: {my_rating}')

while True:
    new_value = int(input('\nEnter new value (for exit -1): '))

    for i, mark in enumerate(my_rating):
        if new_value >= mark:
            my_rating.insert(i, new_value)
            break
        elif new_value == -1:
            break
        elif new_value < my_list[-1]:
            my_rating.append(new_value)
            break

    if new_value == -1:
        print(f'\n-- GAME OVER --')
        break

    print(my_rating)
