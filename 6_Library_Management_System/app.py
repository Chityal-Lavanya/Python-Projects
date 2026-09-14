import json


FILE_NAME = "6_Library_Management_System/library.json"

class LibraryItem:

    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title

    def display_info(self):
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")

class Book(LibraryItem):

    def __init__(self, book_id, title, author, available=True):
        super().__init__(book_id, title)

        self.author = author

        # Encapsulation
        self.__available = available

    # Getter
    def is_available(self):
        return self.__available

    # Issue book
    def issue_book(self):
        if self.__available:
            self.__available = False
            return True

        return False

    # Return book
    def return_book(self):
        if not self.__available:
            self.__available = True
            return True

        return False

    # Display book details
    def display_info(self):
        status = "Available" if self.__available else "Issued"

        print(f"ID     : {self.book_id}")
        print(f"Title  : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")
        print("-" * 30)

class Library:

    def __init__(self):
        self.books = []
        self.load_books()

    # Add book
    def add_book(self):
        book_id = input("Enter book ID: ").strip()

        # Check duplicate ID
        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        book = Book(book_id, title, author)

        self.books.append(book)
        self.save_books()

        print("Book added successfully!")

    # Remove book
    def remove_book(self):
        book_id = input("Enter book ID to remove: ").strip()

        for book in self.books:

            if book.book_id == book_id:

                if not book.is_available():
                    print("Cannot remove an issued book!")
                    return

                self.books.remove(book)
                self.save_books()

                print("Book removed successfully!")
                return

        print("Book not found!")

    # Search book
    def search_book(self):
        keyword = input("Enter book title or author: ").strip().lower()

        found = False

        for book in self.books:

            if (keyword in book.title.lower()
                    or keyword in book.author.lower()):

                book.display_info()
                found = True

        if not found:
            print("No matching books found.")

    # View all books
    def view_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\n===== ALL BOOKS =====")

        for book in self.books:
            book.display_info()

    # Issue book
    def issue_book(self):
        book_id = input("Enter book ID to issue: ").strip()

        for book in self.books:

            if book.book_id == book_id:

                if book.issue_book():
                    self.save_books()
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                return

        print("Book not found!")

    # Return book
    def return_book(self):
        book_id = input("Enter book ID to return: ").strip()

        for book in self.books:

            if book.book_id == book_id:

                if book.return_book():
                    self.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book is already available.")

                return

        print("Book not found!")

    # Save books to JSON file
    def save_books(self):

        data = []

        for book in self.books:

            data.append({
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "available": book.is_available()
            })

        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    # Load books from JSON file
    def load_books(self):

        try:

            with open(FILE_NAME, "r") as file:
                data = json.load(file)

                for item in data:

                    book = Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["available"]
                    )

                    self.books.append(book)

        except FileNotFoundError:
            self.books = []

# Main Program
library = Library()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. View All Books")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.remove_book()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.view_books()

    elif choice == "5":
        library.issue_book()

    elif choice == "6":
        library.return_book()

    elif choice == "7":
        print("Library data saved. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")