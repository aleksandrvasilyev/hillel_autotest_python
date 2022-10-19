from hw9_1 import outer


@outer('hello')
def ifcapital(text):
    """Функция проверяет соответствие результату работы методу capitalize()"""
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
