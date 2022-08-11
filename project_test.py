from library import *

print("""*******************************************

Welcome to the library!!!

Actions you can take;

1. View books
2. Book query
3. Add a book
4. Delete a book
5. Increase the edition

To leave the program please press 'x'

*******************************************
""")

library = Library()

while True:
    action = input("What would you like to do?")

    if action == "x":
        print("Exiting the program... See you later!")
        break

    elif action == "1":
        library.list_books()

    elif action == "2":
        name = input("Which book are you looking for ?")
        print("Looking your book up")
        time.sleep(1)
        library.enquire_book(name)

    elif action == "3":
        name = input("Name of the book:")
        author = input("Author of the book:")
        publisher = input("Publisher of the book:")
        type = input("Type of the book:")
        edition = int(input("Edition:"))

        new_book = Book(name,author,publisher,type,edition)

        print("Adding your book....")

        time.sleep(1)

        library.add_book(new_book)

        print("Your book has been added to our systems...")

    elif action == "4":
        name = input("Which book would you like to delete ?")
        print("Deleting your book....")
        time.sleep(1)
        library.delete_book(name)
        print("Your book has been deleted from our systems...")

    elif action == "5":
        name = input("Which books edition would you like to change?")
        library.change_edition(name)
        print("Edition of your book has been updated...")

    else:
        print("Invalid request!")






























