import time

# Task 1

text = input('Enter some text here ')

for char in text:
    if char.isalpha():
        if char.islower():
            print(f'{char} is a small letter')
        else:
            print(f'{char} is a capital letter')
    elif char.isdigit():
        if int(char) % 2 == 0:
            print(f'{char} is an even number')
        else:
            print(f'{char} is an odd number')
    else:
        print(f'{char} is a symbol')

# Task 2

while True:
    print('I love Python')
    time.sleep(4.2)