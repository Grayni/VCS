with open('dir/s3_stuff.txt', 'r', encoding='utf-8') as f:
    text = f.read().split('\n')
    poor = [w.split()[0] for w in text if float(w.split()[1]) < 20000]

    print(f'Сотрудники с низкой зп: {", ".join(poor)}')
    print('Средняя зп: ', sum([float(s.split()[1]) for s in text])/len(text))
