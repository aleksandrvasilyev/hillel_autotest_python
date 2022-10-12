def my_decorator(func):
    def wrapper(*args, **kwargs):
        res = str(func(*args, **kwargs))

        return res

    return wrapper


@my_decorator
def foo(arg1, arg2):
    print(arg1 * arg2)


foo(2, 3)
