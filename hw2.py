print('Касир в кінотеватрі')

while True:
    age = input('Ваш вік: ')

    if age.isdigit():
        age_int = int(age)
        if age_int < 1:
            print('Вы еще не родились')
        elif age_int < 7:
            print('Де твої батьки?')
        elif age_int < 16:
            print('Це фільм для дорослих!')
        elif age_int > 65:
            print('Покажіть пенсійне посвідчення!')
        elif '7' in age:
            print('Вам сьогодні пощастить!')
        else:
            print('А білетів вже немає!')
    else:
        print('Введіть корректний вік')