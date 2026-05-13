from django.db import models
import pytz

# Create your models here.
class Book(models.Model):

    COVERS = [
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('ebook', 'E-book'),
        ('audiobook', 'Audiobook'),
    ] 

    LANGUAGE = [
        ('english', 'English'),
        ( 'polish', 'Polish'),
        ('german', 'German'),
        ('french', 'French'),
        ('spanish', 'Spanish'),
        ('hebrew', 'Hebrew'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=20, choices=COVERS)
    language = models.CharField(max_length=20, choices=LANGUAGE)
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    authors = models.ManyToManyField('Author', related_name='books')
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT, on_update=models.CASCADE)
    series = models.ForeignKey('Series', on_delete=models.RESTRICT, on_update=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    topic = models.ManyToManyField('Topic', related_name='books', blank=True)
    notes = models.ManyToOneField('Note', related_name='books', blank=True)

class Author(models.Model):
     TITLES = [
        ('ks', 'Ks.'),
        ('dr', 'Dr.'),
        ('prof', 'Prof.'),
        ('bp', 'Bp'),
    ]
     
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100)
    title = models.CharField(max_length=50, choices=TITLES, blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='authors', blank=True)
    series = models.ManyToManyField('Series', related_name='authors', blank=True)
    
class Publisher(models.Model):
        name = models.CharField(max_length=200)
        country = models.CharField(max_length=2, choises=pytz.country_names.items())
        founded_year = models.IntegerField()
        website = models.URLField(blank=True, null=True)
        email = models.EmailField(blank=True, null=True)
        books = models.ManyToOneField(Book, related_name='publishers', blank=True, null=True)

class Genre(models.Model): 
    name = models.CharField(max_length=100) 

class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='series', blank=True)
    authors = models.ManyToManyField(Author, related_name='series', blank=True)

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='topics', blank=True)

class Note(models.Model): 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes')

    