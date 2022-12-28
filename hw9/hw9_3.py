def fibo(goal, current=0, x=0, y=1):
    if current + 1 == goal:
        return x
    current += 1
    return fibo(goal, current, x=y, y=x + y)


while True:
    index = input('Enter the index of the required Fibonacci number\n')
    if index.isdigit():
        if int(index) > 0:
            print(f'The result is {fibo(int(index))}')
        else:
            print('Index must be greater than zero')
    elif index == 'exit':
        break
    else:
        print('Enter an integer and positive number or "exit"\n')