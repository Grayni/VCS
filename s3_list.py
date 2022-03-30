class List:
    @staticmethod
    def create():
        arr = []

        while 1:
            value = input('Введите число или "stop": ')
            if value == 'stop':
                print(arr)
                break
            else:
                try:
                    if value.isdigit():
                        arr.append(int(value))
                    elif value.replace('.', '').isdigit():
                        arr.append(float(value))
                    else:
                        raise ValidNum('Введеное значение должно быть числом.')
                except ValidNum as err:
                    print(err)


class ValidNum(Exception):
    def __init__(self, value):
        self.value = value


lst1 = List().create()
