class MyIterator:
    x = 0
    y = 1
    counter = 0
    stop = 0

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.stop:
            raise StopIteration()
        self.counter += 1
        temp = self.x
        self.x, self.y = self.y, self.x + self.y
        return temp


result = None  # Otherwise python annoy with notification 'Name can be undefined'. And this is only way I can fix that
while True:
    index = input('Enter the index of the required Fibonacci number\n')
    if index.isdigit():
        if int(index) > 0:
            my_iter_obj = MyIterator(int(index))
            for result in my_iter_obj:
                continue
            print(f'The result is {result}')
        else:
            print('Index must be greater than zero')
    elif index == 'exit':
        break
    else:
        print('Enter an integer and positive number or "exit"\n')
