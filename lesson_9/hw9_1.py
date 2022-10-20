def outer(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            myfunc = func(*args, **kwargs)
            print(myfunc, text)
            return myfunc

        return wrapper

    return decorator


@outer('hello')
def paired(num):
    """Функция проверяет парность числа"""
    if type(num) in (int, float):
        return True if num % 2 == 0 else False
    else:
        return False


assert paired(0)
assert paired(4)
assert paired(5) is False
assert paired(8.0)
assert paired(1) is False
assert paired('120') is False