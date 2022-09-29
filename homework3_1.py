while True:
    word = input('Введите слово: ')
    number = input('Введите номер: ')

    try:
        print(f'The {number} symbol in "{word.capitalize()}" is "{word[int(number) - 1]}"')
    except IndexError as e:
        print('Неподходящее число индекса')
    except ValueError as e:
        print('Введите число индекса')
