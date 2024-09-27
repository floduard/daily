import json
import os
from datetime import datetime

class BookStore:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.load_books()

    def load_books(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.books = json.load(f)
            else:
                self.books = []
        except (IOError, json.JSONDecodeError):
            print(f"Error loading books from {self.filename}.")
            self.books = []

    def save_books(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.books, f)
        except IOError:
            print(f"Error saving books to {self.filename}.")

    def is_valid_name(self, text):
        return text[0].isalpha() if text else False  # Ensure the name starts with a letter

    def is_valid_string(self, text):
        return all(c.isalpha() or c.isspace() for c in text)  # Allow spaces, but no numbers

    def is_valid_year(self, year):
        try:
            current_year = datetime.now().year
            return year.isdigit() and int(year) <= current_year
        except ValueError:
            return False

    def add_book(self, name, author, year):
        try:
            if not self.is_valid_name(name):
                raise ValueError("Book name should not start with a number.")
            if not self.is_valid_string(author):
                raise ValueError("Author name should not contain numbers.")
            if not self.is_valid_year(year):
                raise ValueError(f"Year of publication should not be later than {datetime.now().year}.")

            self.books.append({'name': name, 'author': author, 'year': year})
            self.save_books()
            print(f'Book "{name}" added successfully!')

        except ValueError as e:
            print(str(e))

    def view_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\nBooks in Store:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. Name: {book['name']}, Author: {book['author']}, Year: {book['year']}")

    def remove_book(self, name):
        try:
            for book in self.books:
                if book['name'].lower() == name.lower():
                    self.books.remove(book)
                    self.save_books()
                    print(f'Book "{name}" removed successfully!')
                    return
            print(f'Book "{name}" not found.')
        
        except Exception as e:
            print(f"Error removing book: {e}")

    def search_book(self, query):
        results = [book for book in self.books if query.lower() in book['name'].lower() 
                   or query.lower() in book['author'].lower()]
        
        if results:
            print("\nSearch Results:")
            for idx, book in enumerate(results, start=1):
                print(f"{idx}. Name: {book['name']}, Author: {book['author']}, Year: {book['year']}")
        else:
            print("No matching books found.")

    def download_books(self, file_format='txt'):
        if not self.books:
            print("No books available to download.")
            return
        
        filename = f'books.{file_format}'
        try:
            with open(filename, 'w') as f:
                if file_format == 'csv':
                    f.write("Name,Author,Year\n")
                    for book in self.books:
                        f.write(f"{book['name']},{book['author']},{book['year']}\n")
                else:  # default to txt
                    for book in self.books:
                        f.write(f"Name: {book['name']}, Author: {book['author']}, Year: {book['year']}\n")
            print(f'Books downloaded successfully as "{filename}".')
        except IOError:
            print(f"Error downloading books as {filename}.")

def main():
    store = BookStore()

    while True:
        print("\nBook Store Menu:")
        print("1. Add New Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            store.add_book(name, author, year)
        elif choice == '2':
            store.view_books()
        elif choice == '3':
            name = input("Enter the name of the book to remove: ")
            store.remove_book(name)
        elif choice == '4':
            query = input("Enter book name or author to search: ")
            store.search_book(query)
       
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
