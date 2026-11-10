import json
from book import Book


class Library:
    def __init__(self, file_name="books.json"):
        self.file_name = file_name
        self.books = []
        self.next_id = 1
        self.load()

    # save all books to the file
    def save(self):
        data = []
        for book in self.books:
            data.append(book.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # load books from the file
    def load(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.books = []
            for item in data:
                self.books.append(Book.from_dict(item))

            biggest_id = 0
            for book in self.books:
                if book.id > biggest_id:
                    biggest_id = book.id
            self.next_id = biggest_id + 1

            print(f"Loaded books: {len(self.books)}")

        except FileNotFoundError:
            print("No saved file yet, starting with an empty library")

        except (json.JSONDecodeError, KeyError, TypeError):
            print("File has wrong data, starting with an empty library")
            self.books = []

    # find one book by id
    def find_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None

    # add a book
    def add_book(self, title, author, year):
        book = Book(self.next_id, title, author, year)
        self.books.append(book)
        self.next_id = self.next_id + 1
        self.save()
        print(f"Book added with id {book.id}")

    # show all books
    def show_all(self):
        if self.books == []:
            print("Library is empty")
        else:
            for book in self.books:
                print(book)

    # search by title
    def search_by_title(self, text):
        found = []
        for book in self.books:
            if text.lower() in book.title.lower():
                found.append(book)
        self.print_results(found)

    # search by author
    def search_by_author(self, text):
        found = []
        for book in self.books:
            if text.lower() in book.author.lower():
                found.append(book)
        self.print_results(found)

    # print search results
    def print_results(self, found):
        if found == []:
            print("Nothing found")
        else:
            for book in found:
                print(book)

    # change availability
    def toggle_availability(self, id):
        book = self.find_by_id(id)
        if book is None:
            print("Book not found")
        else:
            book.is_available = not book.is_available
            self.save()
            print("Status changed:", book)

    # delete a book
    def delete_book(self, id):
        book = self.find_by_id(id)
        if book is None:
            print("Book not found")
        else:
            self.books.remove(book)
            self.save()
            print("Book deleted")

    # edit a book (empty field = keep old value)
    def edit_book(self, id, title, author, year):
        book = self.find_by_id(id)
        if book is None:
            print("Book not found")
            return

        if title != "":
            book.title = title
        if author != "":
            book.author = author
        if year is not None:
            book.year = year

        self.save()
        print("Book updated:", book)