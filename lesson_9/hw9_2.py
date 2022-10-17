def outer(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            """Функция проверяет соответствие результату работы методу capitalize()"""
            myfunc = func(*args, **kwargs)
            print(myfunc, text)
            return func
        return wrapper
    return decorator


@outer('hello')
def ifcapital(text):
    if type(text) == str:
        return True if text.capitalize() == text else False
    else:
        return False


assert ifcapital('Привет')
assert ifcapital('привет')
assert ifcapital('')
assert ifcapital('lorem ipsum')
assert ifcapital('123')
assert ifcapital(123)
print(ifcapital.__doc__)
