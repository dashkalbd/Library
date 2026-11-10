from library import Library


# ask until the user types a real number
def ask_number(text):
    while True:
        answer = input(text)
        try:
            return int(answer)
        except ValueError:
            print("Please enter a number")


def menu():
    library = Library()

    while True:
        print()
        print("1 - Add book")
        print("2 - Show all books")
        print("3 - Search by title")
        print("4 - Search by author")
        print("5 - Change availability")
        print("6 - Delete book")
        print("7 - Edit book")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = ask_number("Year: ")
            library.add_book(title, author, year)

        elif choice == "2":
            library.show_all()

        elif choice == "3":
            text = input("Title contains: ")
            library.search_by_title(text)

        elif choice == "4":
            text = input("Author contains: ")
            library.search_by_author(text)

        elif choice == "5":
            id = ask_number("Book id: ")
            library.toggle_availability(id)

        elif choice == "6":
            id = ask_number("Book id: ")
            library.delete_book(id)

        elif choice == "7":
            id = ask_number("Book id: ")
            print("Leave a field empty to keep it")
            title = input("New title: ")
            author = input("New author: ")
            year_text = input("New year: ")
            if year_text.isdigit():
                year = int(year_text)
            else:
                year = None
            library.edit_book(id, title, author, year)

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Wrong choice, try again")


menu()