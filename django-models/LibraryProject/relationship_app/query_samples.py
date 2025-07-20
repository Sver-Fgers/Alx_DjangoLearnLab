# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", list(books_by_author))

# Query 2: All books in a specific library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", list(books_in_library))

# Query 3: The librarian of a specific library
librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian.name)
