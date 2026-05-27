from django.shortcuts import HttpResponse, render
from manage_books.models import Book, Author, Publisher, Series, Note

def index(request):
    books = Book.objects.all()
    return render(request, 'manage_books/index.html.jinja', {'books': books})

def book(request, book_id):
    return render(request, 'manage_books/book.html.jinja', {'book_id': book_id})

def author(request, author_id):
    return render(request, 'manage_books/author.html.jinja', {'author_id': author_id})

def publisher(request, publisher_id):
    return render(request, 'manage_books/publisher.html.jinja', {'publisher_id': publisher_id})

def series(request, series_id):
    return render(request, 'manage_books/series.html.jinja', {'series_id': series_id})

def note(request, note_id):
    return render(request, 'manage_books/note.html.jinja', {'note_id': note_id})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'manage_books/authors.html.jinja', {'authors': authors})

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'manage_books/publishers.html.jinja', {'publishers': publishers})

def series_list(request):
    series = Series.objects.all()
    return render(request, 'manage_books/series_list.html.jinja', {'series': series})

def notes(request):
    notes = Note.objects.all()
    return render(request, 'manage_books/notes.html.jinja', {'notes': notes})