while True:
    word = input('Введите слово: ')
    letters = ['o', 'O', 'о', 'О']

    if any([letter in word for letter in letters]):
        print('it\'s ok')
        break
    else:
        print('В слове должна быть буква "о"')
