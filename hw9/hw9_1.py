def my_fib_func(n):
    x = 0
    y = 1
    for j in range(n):
        yield x
        x, y = y, x + y


result = None  # Otherwise python annoy with notification 'Name can be undefined'. And this is only way I can fix that
while True:
    index = input('Enter the index of the required Fibonacci number\n')
    if index.isdigit():
        if int(index) > 0:
            for result in my_fib_func(int(index)):
                pass
            print(f'The result is {result}')
        else:
            print('Index must be greater than zero')

    elif index == 'exit':
        break
    else:
        print('Enter an integer and positive number or "exit"\n')
