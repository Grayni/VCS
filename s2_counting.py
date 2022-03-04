with open('dir/s2_counting.txt', 'r', encoding='utf-8') as f:
    text = f.read().split('\n')
    [print(f'{i}.', f'words {len(x.split())};', x) for i, x in enumerate(text, 1)]
    print(f'\nStrings: {len(text)}')
