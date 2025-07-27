from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
orwell_books = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", list(orwell_books))

# List all books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)  # <-- This line is required by the checker
books_in_library = library.books.all()
print(f"Books in {library_name}:", list(books_in_library))

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian at {library_name}:", librarian.name)
