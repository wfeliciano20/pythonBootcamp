books = []


def add_book(name, author):
    data = {"name": name, "author": author, "read": False}
    books.append(data)


def list_books():
    if len(books) > 0:
        for book in books:
            print(book)
    else:
        print("Thera are no books")


def read_book(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True


def delete_book(name):
    global books
    if len(books) == 0:
        print("There are no books to delete")
    if len(books) > 0:
        books = [book for book in books if book["name"] != name]
    elif len(books) == 1:
        for book in books:
            if book["name"] == name:
                books.pop()


books_file = 'books.txt'


def add_book_to_file(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},False\n')


def get_all_books_from_file():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return [
        {'name': line[0], 'author':line[1], 'read':line[2]}
        for line in lines
    ]


def mark_book_as_read_from_file(name):
    books = get_all_books_from_file()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books_to_file(books)


def _save_all_books_to_file(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book_from_file(name):
    books = get_all_books_from_file()
    books = [book for book in books if book['name'] != name]
    _save_all_books_to_file(books)
