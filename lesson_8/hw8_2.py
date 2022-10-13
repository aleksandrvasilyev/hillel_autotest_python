def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Convert to string the result of the function of multiplying two numbers """
        res = str(func(*args, **kwargs))

        return res

    return wrapper


@my_decorator
def foo(arg1, arg2):
    return arg1 * arg2


foo(2, 3)
print(foo.__doc__)
