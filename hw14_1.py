import re

user_input = input('Enter file name in format File.txt \n')

try:
    with open(f'{user_input}', 'r+') as file:
        text = file.read()
        text = re.sub(r"(?<=\s)(?P<first>\w)[\w.]{2,}@\w+\.[\w.]+(?P<last>\w)(?=[ ,.]|$|\n)",
                      r"\g<first>***@***\g<last>", text)

        file.truncate(0)
        file.seek(0)
        file.write(text)
except FileNotFoundError:
    print('File doesn\'t exist')
