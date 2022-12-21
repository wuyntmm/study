my_dict = {
    'Fireman': 101,
    'Police': 102,
    'Ambulance': 103
}


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

    users_input = input('What do you want to do? ')

    match users_input.split()[0]:
        case 'stats':
            stats()
        case 'add':
            if len(users_input.split()) > 2:
                add(users_input.split()[1], users_input.split()[2])
            else:
                print('Please enter the line in format \'add Name Number\'')
        case 'delete':
            if len(users_input.split()) > 1:
                delete(users_input.split()[1])
            else:
                print('Please enter the line in format \'delete Name\'')
        case 'list':
            names()
        case 'show':
            if len(users_input.split()) == 2:
                show(users_input.split()[1])
            elif len(users_input.split()) > 2:
                print('There are no', end=' ')
                for item in users_input.split():
                    print(item, end=' ')
                print('in this dictionary')
            else:
                print('Please enter the line in format \'show Name\'')
        case 'exit':
            break
        case _:
            print('I don\'t understand you. Please use commands: stats, add, delete, list, show or exit')
