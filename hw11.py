import time


def name_and_time(func):
    print(f'You called function "{func.__name__}" on {time.ctime()}')

    def inner_deco_func():
        func()

    return inner_deco_func


class MyCustomException(Exception):
    pass


class MyCtxManager:
    def __enter__(self):
        print('==========')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'There are some problem here: {exc_val}')
        print('==========')
        return True


@name_and_time
def universal_func():
    arr = [1, 3, 5, 10, 0]
    result = []
    for i in arr:
        if i != 0:
            print(15 / i)
            result.append(15 / i)
        else:
            raise MyCustomException(f'Custom exception is occurred. You tried dividing by {i}')


with MyCtxManager():
    universal_func()

try:
    print('==========')
    universal_func()
except MyCustomException as ex:
    print(f'There are some problem here: {ex}')
except Exception as un_ex:
    print(f'Unknown exception: {un_ex}')
else:
    print('There are was no errors in the code')
finally:
    print('==========')
