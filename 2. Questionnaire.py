# Questionnaire
u_name = input('Ваше имя: ')
u_surname = input('Ваша фамилия: ')
u_born = input('Дата рождения: ')
u_city = input('Откуда вы: ')
u_email = input('Ваша почта: ')
u_phone = input('Номер телефона: ')


def show_data(name='-', surname='-', born='-', city='-', email='-', phone='-'):
    print(', '.join([name, surname, born, city, email, phone]))


show_data(surname=u_surname, born=u_born, name=u_name, city=u_city, email=u_email, phone=u_phone)
