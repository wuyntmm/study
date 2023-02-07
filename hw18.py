class Bot:
    def __init__(self, name):
        self.name = name

    def send_message(self, message):
        print(message)

    def say_name(self):
        print(self.name)


class TelegramBot(Bot):
    url = chat_id = None

    def set_url(self, url):
        self.url = url

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f'TG bot said {message} to {self.chat_id} in {self.url}')


some_bot = Bot('Bot1')
some_bot.say_name()
some_bot.send_message('Wath\'s up')

tg_bot = TelegramBot('Robin')
tg_bot.say_name()
tg_bot.send_message('Hi!')
tg_bot.set_chat_id(21)
tg_bot.set_url('web.telegram.com')
tg_bot.send_message('Hello')


class MyStr(str):
    def __str__(self):
        return super().__str__().upper()


my_str = MyStr('test')
print(my_str)


class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return str(self.name).lower() == str(other.name).lower()


first_user = User('OLEKSII')

second_user = User('Oleksii')

print(first_user == second_user)


def init_alternative(self, name):
    self.name = name


def send_massage_func(self, message):
    print(message)


def say_name_func(self):
    print(self.name)


Bot_type = type(
    'NewBotClass',
    (),
    {
        '__init__': init_alternative,
        'send_message': send_massage_func,
        'say_name': say_name_func
    }

)

new_bot = Bot_type('Jack')
new_bot.say_name()
new_bot.send_message('Hi!')


def set_url_func(self, url):
    self.url = url


def set_chat_id_func(self, chat_id):
    self.chat_id = chat_id


def send_message_func_new(self, message):
    print(f'I just said {message} to {self.chat_id} with {self.url}')


TelegramBot_type = type(
    'NewTGBot',
    (Bot_type,),
    {
        'url': None,
        'chat_id': None,
        'send_message': send_message_func_new,
        'set_url': set_url_func,
        'set_chat_id': set_chat_id_func

    }

)

tg_bot = TelegramBot_type('John')
tg_bot.say_name()
tg_bot.send_message('Hi!')
tg_bot.set_chat_id(21)
tg_bot.set_url('web.telegram.com')
tg_bot.send_message('Hello')
