# Firm / Part 2
revenue = int(input('Введите выручку вашей фирмы: '))
costs = int(input('Введите издержки вашей фирмы: '))
profit = revenue - costs
if revenue > costs:
    print(f'Рентабельность выручки: {profit / revenue}')
else:
    print('Фирма не прибыльна')

print('')
employees = int(input('Введите количество ваших сотрудников: '))


print(f'Прибыль на 1 сотрудника: {profit / employees} y.e.')
