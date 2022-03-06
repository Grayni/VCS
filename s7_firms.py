import json

with open('dir/s7_firms.txt', 'r', encoding='utf-8') as f:
    firms = {}
    profit = {'average_profit': 0}
    counter = 0

    while True:
        line = f.readline()[:-1]

        if not line:
            profit['average_profit'] = round(profit['average_profit'] / counter)
            break

        lst = line.split(' ')
        profit_firm = int(lst[2]) - int(lst[3])

        if profit_firm >= 0:
            counter += 1
            profit['average_profit'] += profit_firm

        firms[lst[0]] = profit_firm

    print([firms, profit])

    with open('dir/s7_firms.json', 'w', encoding='utf-8') as j:
        json.dump([firms, profit], j)



