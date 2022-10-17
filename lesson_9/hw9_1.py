def outer(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """Функция проверяет парность числа"""
            myfunc = func(*args, **kwargs)
            print(myfunc, text)
            return func
        return wrapper
    return decorator


@outer('hello')
def paired(num):
    if type(num) in (int, float):
        return True if num % 2 == 0 else False
    else:
        return False


assert paired(0)
assert paired(4)
assert paired(5)
assert paired(8.0)
assert paired(1.5)
assert paired('120')
print(paired.__doc__)

