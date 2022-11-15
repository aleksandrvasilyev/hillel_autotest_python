while True:
    word = input('Введите слово: ')
    number = input('Введите номер: ')
    letters = ['o', 'O', 'о', 'О']

    if any([i in word for i in letters]):
        try:
            print(f'The {number} symbol in "{word}" is "{word[int(number) - 1]}"')
            break
        except IndexError as e:
            print('Неподходящий индекс')
        except ValueError as e:
            print('Неверное значение идекса')
    else:
        print('Слово должно включать "о" или "О"')
