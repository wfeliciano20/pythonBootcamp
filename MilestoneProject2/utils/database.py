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
