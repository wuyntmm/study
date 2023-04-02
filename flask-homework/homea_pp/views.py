from .__init__ import app
import random
from flask import request, redirect


@app.route('/hello')
def index():
    app.logger.info('INFO was logged successfully')
    return 'Hello, world!'


@app.get('/users')
def get_users():
    names = ["Emily", "Jacob", "Ava", "Mia", "Noah", "Ethan", "Isabella", "Oliver", "Sophia", "Charlotte"]
    res = '<ul>'
    for i in range(random.randint(2, 10)):
        res += f'<li>{random.choice(names)}</li>'
    res += '</ul>'
    return res, 200


@app.get('/books')
def get_book():
    books = [
        "To Kill a Mockingbird by Harper Lee",
        "1984 by George Orwell",
        "The Catcher in the Rye by J.D. Salinger",
        "The Great Gatsby by F. Scott Fitzgerald",
        "Pride and Prejudice by Jane Austen",
        "One Hundred Years of Solitude by Gabriel Garcia Marquez",
        "The Hitchhiker's Guide to the Galaxy by Douglas Adams",
        "The Hobbit by J.R.R. Tolkien",
        "The Lord of the Rings by J.R.R. Tolkien",
        "The Da Vinci Code by Dan Brown"
    ]
    res = '<ul>'
    for i in range(random.randint(2, 10)):
        res += f'<li>{random.choice(books)}</li>'
    res += '</ul>'
    return res, 200


@app.get('/users/<int:users_id>')
def get_users_by_id(users_id):
    if users_id % 2:
        return '<h1>Not Found</h1>', 404
    else:
        return f'<div>Your ID: {users_id}', 200


@app.get('/books/<string:title>')
def get_book_title(title):
    return f'<h1>{str(title).title()}</h1>', 200


@app.route('/params')
def get_params():
    params = request.args.to_dict()
    table = '<table><tr><th>parameter</th><th>value</th></tr>'
    for key, value in params.items():
        table += f'<tr><td>{key}</td><td>{value}</td></tr>'
    table += '</table>'
    return table, 200


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        form = '''
        <form method="post" action="/login">
            <label>Username:</label>
            <input type="text" name="username"><br><br>
            <label>Password:</label>
            <input type="password" name="password"><br><br>
            <button type="submit">Send form</button>
        </form>
        '''
        return form, 200

    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            return '<h1>Data is missing</h1>', 400


@app.errorhandler(404)
def page_not_found(e):
    app.logger.info(f'{e.name} occurs')
    return '<h1>Exception 404 :(</h1>', 404


@app.errorhandler(500)
def internal_server_error(e):
    app.logger.info(f'{e.name} occurs')
    return '<h1>Exception 500, try again</h1>', 500