# Structure "Products"
lst = []
obj = {'название': '', 'цена': 0, 'количество': 0, 'ед': ''}
i = 0

# create survey
while True:
    card = obj.copy()

    i += 1

    print('\nЗаполните карточку товара')
    for key in card:
        value = input(f'{key}: ')
        # check int and assign
        card[key] = int(value) if key in ['цена', 'количество'] else value

    tup = (i, card)
    lst.append(tup)

    print('\nКарточка создана')
    print(f'{tup}\n\n')

    value = input('Создать еще карточку n/Y? ')
    if value == 'Y' or value == 'y' or value == '':
        continue
    else:
        break


# show database of products
print('\n-- БАЗА ТОВАРОВ --')

for x in lst:
    print(x)


# create skeleton of data analytics
analytics_data = obj.copy()

# dynamically change type in obj of key
for name in analytics_data:
    analytics_data[name] = []  # I know. or create new pure obj

# add values in skeleton of analytics
for product in lst:
    for name in product[1]:
        # unique values
        if not product[1][name] in analytics_data[name]:
            analytics_data[name].append(product[1][name])

print('\n\n-- АНАЛИТИКА --\n{')
for name in analytics_data:
    print(f'    {name}: {analytics_data[name]}')
print('}')
