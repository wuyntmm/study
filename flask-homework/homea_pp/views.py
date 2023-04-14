from . import app
import os
import random
from flask import request, redirect, render_template, session, url_for, abort
from .models import User, Book, Purchase

app.secret_key = os.getenv('SECRET_KEY')
@app.route('/hello')
def index():
    app.logger.info('INFO was logged successfully')
    return 'Hello, world!'


@app.get('/users')
def get_users():
    user = session.get('user')
    if user:
        all_users = User.query.all()
        dict_users = [{
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age
        } for user in all_users]
        if 'size' in request.args:
            return dict_users[:int(request.args.get('size'))]
        return dict_users, 200
    else:
        return redirect('/login')


@app.get('/books')
def get_book():
    user = session.get('user')
    if user:
        all_books = Book.query.all()
        dict_books = [{
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year': book.year,
            'price': book.price
        } for book in all_books]
        if 'size' in request.args:
            return dict_books[:int(request.args.get('size'))]
        return dict_books, 200
    else:
        return redirect('/login')

@app.get('/users/<int:user_id>')
def get_users_by_id(user_id):
    user = session.get('user')
    if user:
        all_users = User.query.all()
        for user in all_users:
            if user.id == user_id:
                user1 = [{
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'age': user.age
                }]
                return user1
    else:
        return redirect('/login')

@app.get('/books/<int:book_id>')
def get_book_title(book_id):
    user = session.get('user')
    if user:
        all_books = Book.query.all()
        for book in all_books:
            if book.id == book_id:
                book1 = [{
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'year': book.year,
                    'price': book.price
                }]
                return book1, 200
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

@app.get('/purchase')
def purchase():
    all_purchase = Purchase.query.all()
    dict_purchase = []
    for purchase_1 in all_purchase:
        all_books = Book.query.all()
        book1 = [book for book in all_books if purchase_1.book_id == book.id]
        all_users = User.query.all()
        user1 = [user for user in all_users if purchase_1.user_id == user.id]
        purchase_2 = {
            'id': purchase_1.id,
            'user_id': purchase_1.user_id,
            'book_id': purchase_1.book_id,
            'date': purchase_1.date,
            'title': book1[0].title,
            'first_name': user1[0].first_name,
            'last_name': user1[0].last_name
        }
        dict_purchase.append(purchase_2)
    if 'size' in request.args:
        return dict_purchase[:int(request.args.get('size'))]
    return dict_purchase

@app.get('/purchase/<int:purchases_id>')
def purchase_id(purchases_id):
    all_purchase = Purchase.query.all()
    for purchase1 in all_purchase:
        if purchase1.id == purchases_id:
            all_books = Book.query.all()
            book1 = [book for book in all_books if purchase1.book_id == book.id]
            all_users = User.query.all()
            user1 = [user for user in all_users if purchase1.user_id == user.id]
            purchase_1 = [{
                'id': purchase1.id,
                'user_id': purchase1.user_id,
                'book_id': purchase1.book_id,
                'date': purchase1.date,
                'title': book1[0].title,
                'first_name': user1[0].first_name,
                'last_name': user1[0].last_name
            }]
            return purchase_1
    return abort(404)
