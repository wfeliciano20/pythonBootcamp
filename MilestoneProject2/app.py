from utils import database


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
    database.add_book(name, author)


def prompt_read_book():
    name = input("Enter the book name: ")
    database.read_book(name)


def prompt_delete_book():
    name = input("Enter the book name that you want to delete: ")
    database.delete_book(name)


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            database.list_books()
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
