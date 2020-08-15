from utils import database
from utils import database2 as db2
from os import path


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:
"""


def prompt_add_book():
    name = input("Enter the name of the book: ")
    author = input("Enter the author name ")
    database.add_book_to_file(name, author)
    db2.add_book(name, author)


def list_books():
    books = database.get_all_books_from_file()
    books = db2.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']},read: {read}")


def prompt_read_book():
    name = input("Enter the book name: ")
    database.mark_book_as_read_from_file(name)
    db2.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the book name that you want to delete: ")
    database.delete_book_from_file(name)
    db2.delete_book(name)


def menu():
    if path.exists('books.json'):
        pass
    else:
        db2.create_book_table()
    if path.exists('books.txt'):
        pass
    else:
        database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        elif user_input == 'q':
            break
        else:
            print("Please enter a valid value")
        user_input = input(USER_CHOICE)


menu()

# def prompt_add_bool()     ask for book name and author
# def list_books()          show all the books in out list
# def prompt_read_book()    ask for book name and change it to "read" in out list
# def prompt_delete_book()  ask for book name and remove book from list
