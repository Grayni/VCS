# Firm

revenue = int(input('Введите выручку вашей фирмы: '))
costs = int(input('Введите издержки вашей фирмы: '))

if revenue > costs:
    print('У вас прибыльная фирма')
elif revenue < costs:
    print('У вас убыточная фирма')
else:
    print('Ваша фирма не имеет прибыли и убытков')