
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.title == book.title:
                print("ეს წიგნი უკვე დამატებულია!")
                return

        self.books.append(book)
        print(f"წიგნი {book.title} წარმატებით დაემატა!")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"წიგნი {title} წაიშალა!")
                return

        print("ასეთი წიგნი ბიბლიოთეკაში არ მოიძებნა!")

    def list_books(self):
        if not self.books:
            print("ბიბლიოთეკა ცარიელია!")
        else:
            for book in self.books:
                print(f"სათაური: {book.title}, ავტორი: {book.author}, წელი: {book.year}")


library = Library()

book1 = Book("Harry Potter", "J.K. Rowling", 1997)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
book3 = Book("1984", "George Orwell", 1949)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_book(book1)

print("\nყველა წიგნი:")
library.list_books()

print("\nწიგნის წაშლა:")
library.remove_book("1984")

print("\nგანახლებული ბიბლიოთეკა:")
library.list_books()
