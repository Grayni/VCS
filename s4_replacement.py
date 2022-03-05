with open('dir/s4_replacement_en.txt', 'r', encoding='utf-8') as f:

    # dict
    nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

    # create new file
    new_f = open('dir/s4_replacement_ru.txt', 'w', encoding='utf-8')

    # enumeration of strings
    while True:
        s = f.readline()

        # check empty
        if not s:
            break

        # get key in old string
        key = s.split(' — ')[0]

        # create new string with replace word [en->ru][use dict]
        s_new = s.replace(f'{key}', f'{nums[key]}')

        # if new str != old str (optional)
        if s_new != s:
            # add new str in new file
            new_f.write(s_new)
    # close new file
    new_f.close()

# close old file
