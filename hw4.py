text = input('Enter the line ')
if len(text) != 0:
    if text.isdigit():
        print('You have entered a number and ', end='')
        if int(text) % 2 == 0:
            print('your number is even')
        else:
            print('your number is odd')
    else:
        length = len(text)
        print(f'You entered a text with a length of {length} characters')
else:
    print('You didn\'t entered any line')
