# Converting seconds to HH:mm:ss

seconds = int(input('Введите число в секундах: '))
time = ''
sec = 3600

while sec > 0:
    # Unit of time
    unit = seconds // sec

    if unit < 10:
        unit = f'0{unit}'

    # The seconds for the next iteration
    seconds %= sec

    # Lover sec for change unit.
    sec = int(sec / 60)

    # Add unit in string 'time'
    time += f'{unit}'
    if sec >= 1:
        time += ':'

print(time)
