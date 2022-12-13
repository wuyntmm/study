text = input('Enter some text here ')

for char in text:
    match char.isdigit():
        case True:
            match int(char) % 2 == 0:
                case True:
                    print(f'{char} is an even number')
                case False:
                    print(f'{char} is an odd number')
        case False:
            match char.isalpha():
                case True:
                    match char.islower():
                        case True:
                            print(f'{char} is a small letter')
                        case False:
                            print(f'{char} is a capital letter')
                case False:
                    print(f'{char} is a symbol')
