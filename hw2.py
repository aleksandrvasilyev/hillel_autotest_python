print('Касир в кінотеватрі')

age = input('Ваш вік: ')

if age.isdigit():
    age = int(age)
    if age < 7:
        print('Де твої батьки?')
    elif age < 16:
        print('Це фільм для дорослих!')
    elif age > 65:
        print('Покажіть пенсійне посвідчення!')
    elif '7' in str(age):
        print('Вам сьогодні пощастить!')
    else:
        print('А білетів вже немає!')
else:
    print('Введіть вік')