import time


def name_and_time(func):

    def inner_deco_func(*args, **kwargs):
        with open('call_log.txt', 'a') as file:
            print(f'You called function "{func.__name__}" on {time.ctime()}', file=file)
        return func(*args, **kwargs)

    return inner_deco_func


@name_and_time
def test():
    print('Test')
    raise MyCustomException('Houston, we have a problem')


class MyCustomException(Exception):
    def __init__(self, message):
        with open('exception_log.txt', 'a') as file:
            print(f'{message} on {time.ctime()}', file=file)
        super().__init__(message)


try:
    test()
except MyCustomException as ex:
    print(f'There was custom exception: {ex}')