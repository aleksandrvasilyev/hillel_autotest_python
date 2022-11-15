print('Касир в кінотеатрі')


def declination(age):
    age = int(age)
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        return 'рік'
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
        return 'роки'
    else:
        return 'років'


def know_age(age):
    if age.isdigit():
        age_int = int(age)
        if age_int < 1:
            print('Вы еще не родились')
        elif '7' in age:
            print(f'Вам {age} {declination(age)}, вам пощастить')
        elif age_int < 7:
            print(f'Тобі ж {age} {declination(age)}! Де твої батьки?')
        elif age_int < 16:
            print(f'Тобі лише {age} {declination(age)}, а це е фільм для дорослих!')
        elif age_int > 65:
            print(f'Вам {age} {declination(age)}? Покажіть пенсійне посвідчення!')
        else:
            print(f'Незважаючи на те, що вам {age} {declination(age)}, білетів всеодно нема!')
    else:
        print('Введіть корректний вік')


while True:
    age = input('Ваш вік: ')
    know_age(age)
