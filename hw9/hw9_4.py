def my_factorial(n):
    if not n:
        return 1
    return n * my_factorial(n - 1)


while True:
    index = input('Enter the index of the required Fibonacci number\n')
    if index.isdigit():
        print(f'The result is {my_factorial(int(index))}')
    elif index == 'exit':
        break
    else:
        print('Enter an integer and positive number or "exit"\n')
