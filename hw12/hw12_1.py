import json
import re

try:
    with open('phonebook.json') as file:
        print('Phonebook successful loaded')
except FileNotFoundError:
    phonebook = {
        'Fireman': '101',
        'Policeman': '102',
        'Doctor': '103'
    }
    print('There are no phonebook yet, let\'s create the new one')
    with open('phonebook.json', 'x+') as file:
        file.write(json.dumps(phonebook))

with open('phonebook.json', 'r+') as file:
    my_dict = json.loads(file.read())

    def stats():
        print(len(my_dict))


    def add(key, value):
        if my_dict.get(key) is None:
            my_dict[key] = value
            print(f'{key} was successful added to the dictionary')
        else:
            print('You are not allowed to edit')


    def delete(key):
        if my_dict.get(key) is not None:
            del my_dict[key]
            print(f'{key} successfully deleted')
        else:
            print(f'There are no {key} in this dictionary')


    def names():
        for item in my_dict.keys():
            print(item)


    def show(key):
        if my_dict.get(key) is not None:
            print(my_dict.get(key))
        else:
            print(f'There are no {key} in this dictionary')


    while True:

        users_input = input('What do you want to do? ').split()

        match users_input[0]:
            case 'stats':
                stats()
            case 'add':
                if len(users_input) > 2:
                    if re.search(r'(\+38|38)?0\d{9}\b', users_input[2]):
                        add(users_input[1], users_input[2])
                    else:
                        print('Invalid number, please enter our number in format +380xxxxxxxxx')
                else:
                    print('Please enter the line in format \'add Name (+380xxxxxxxxx)\'')
            case 'delete':
                if len(users_input) > 1:
                    delete(users_input[1])
                else:
                    print('Please enter the line in format \'delete Name\'')
            case 'list':
                names()
            case 'show':
                if len(users_input) == 2:
                    show(users_input[1])
                elif len(users_input) > 2:
                    print('There are no', end=' ')
                    for item in users_input:
                        print(item, end=' ')
                    print('in this dictionary')
                else:
                    print('Please enter the line in format \'show Name\'')
            case 'exit':
                break
            case _:
                print('I don\'t understand you. Please use commands: stats, add, delete, list, show or exit')
    file.truncate(0)
    file.seek(0)
    file.write(json.dumps(my_dict))
