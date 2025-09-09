class Book:
    def __init__(self, tittle, author):
        self.tittle = tittle
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.tittle} ha sido prestado.")
        else:
            print(f"El libro {self.tittle} no está disponible.")
    
    def return_book(self):
        self.available = True
        print(f"El libro {self.tittle} ha sido devuelto.")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.tittle} no está disponible.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book
            self.borrowed_books.remove(book)
            print(f"El libro {book.tittle} ha sido devuelto.")
        else:
            print(f"El libro {book.tittle} no está en la lista de prestados.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.tittle} ha sido agregado.")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado.")

    def show_available_books(self):
        print(f"Libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f"{book.tittle} por {book.author}")

#Llamada a los métodos
#Crear los libros
book1 = Book("Principito", "Antoine")
book2 = Book("1984", "George Orwell")

#Crear los usuarios
user1 = User("Allisson", "001")

#Crear biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Mostrar libros
library.show_available_books()

#Realizar préstamo
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()

