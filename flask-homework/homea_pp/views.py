from .__init__ import app
import random
from flask import request, redirect, render_template, session, url_for

app.secret_key = b'1234'
@app.route('/hello')
def index():
    app.logger.info('INFO was logged successfully')
    return 'Hello, world!'


@app.get('/users')
def get_users():
    user = session.get('user')
    if user:
        names = ["Emily", "Jacob", "Ava", "Mia", "Noah", "Ethan", "Isabella", "Oliver", "Sophia", "Charlotte"]
        random_names = []
        for i in range(random.randint(2, 10)):
            random_names.append(random.choice(names))
        return render_template('users.html', random_names=random_names, user=user), 200
    else:
        return redirect('/login')


@app.get('/books')
def get_book():
    user = session.get('user')
    if user:
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
        books_list = []
        for i in range(random.randint(2, 10)):
            books_list.append(random.choice(books))
        return render_template('books.html', books_list=books_list, user=user), 200
    else:
        return redirect('/login')

@app.get('/users/<int:users_id>')
def get_users_by_id(users_id):
    user = session.get('user')
    if user:
        if users_id % 2:
            return render_template('user_not_found.html', user=user), 404
        else:
            return render_template('user_id.html', users_id=users_id, user=user)
    else:
        return redirect('/login')

@app.get('/books/<string:title>')
def get_book_title(title):
    user = session.get('user')
    if user:
        return render_template('books_title.html', title=str(title).title(), user=user), 200
    else:
        return redirect('/login')

@app.route('/params')
def get_params():
    user = session.get('user')
    if user:
        params = request.args.to_dict()
        return render_template('params.html', params=params, user=user)
    else:
        return redirect('/login')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html'), 200

    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            session['user'] = username
            session['password'] = password
            return redirect('/users')
        else:
            return render_template('login_fail.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    app.logger.info(f'{e.name} occurs')
    return '<h1>Exception 404 :(</h1>', 404


@app.errorhandler(500)
def internal_server_error(e):
    app.logger.info(f'{e.name} occurs')
    return '<h1>Exception 500, try again</h1>', 500

@app.post('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))
