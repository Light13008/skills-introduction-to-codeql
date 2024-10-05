
from flask import request, render_template
from server.webapp import flaskapp, cursor
from server.models import Book

@flaskapp.route('/')
def index():
    name = request.args.get('name')
    author = request.args.get('author')
    read = request.args.get('read')  # This will be a string, convert to bool if needed

    # Initialize an empty list for books
    books = []

    if name:
        cursor.execute("SELECT * FROM books WHERE name LIKE %s", ('%' + name + '%',))
        books = [Book(*row) for row in cursor]

    elif author:
        cursor.execute("SELECT * FROM books WHERE author LIKE %s", ('%' + author + '%',))
        books = [Book(*row) for row in cursor]

    else:
        cursor.execute("SELECT name, author, read FROM books")
        books = [Book(*row) for row in cursor]

    return render_template('books.html', books=books)
