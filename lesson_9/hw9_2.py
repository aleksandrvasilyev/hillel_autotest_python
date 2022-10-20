from hw9_1 import outer


@outer('hello')
def ifcapital(text):
    """Функция проверяет соответствие результату работы методу capitalize()"""
    if type(text) == str:
        return True if text.capitalize() == text else False
    else:
        return False


print()
assert ifcapital('Привет')
assert ifcapital('привет') is False
assert ifcapital('')
assert ifcapital('lorem ipsum') is False
assert ifcapital('123')
assert ifcapital(123) is False
