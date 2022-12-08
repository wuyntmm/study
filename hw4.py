text = input('Enter the line ')
if len(text) != 0:
    if text.isdigit():
        print('You have entered a number and your number is', end=' ')
        if int(text) % 2 == 0:
            print('even')
        else:
            print('odd')
    else:
        print(f'You entered a text with a length of {len(text)} characters')
else:
    print('You didn\'t entered any line')
