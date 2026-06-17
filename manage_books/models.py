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

    LANGUAGES = [
        ('english', 'English'),
        ("polish", 'Polish'),
        ('spanish', 'Spanish'),
        ('french', 'French'),
        ('german', 'German'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=20, choices=COVERS)
    language = models.CharField(max_length=20, choices=LANGUAGES)
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    authors = models.ManyToManyField('Author', related_name='books', blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT)
    series = models.ForeignKey('Series', on_delete=models.RESTRICT, blank=True, null=True)
    genres = models.ManyToManyField('Genre', related_name='books', blank=True)
    topics = models.ManyToManyField('Topic', related_name='books', blank=True)

    @property
    def authors_display(self):
        return ", ".join(a.full_name for a in self.authors.all())

class Author(models.Model):
    TITLES = [
            ('ks', "Ks."),
            ('dr', "Dr."),
            ('prof', "Prof."),
            ('mr', "Mr."),
            ('ms', "Ms."),
        ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    title = models.CharField(max_length=20, choices=TITLES, blank=True, null=True)
    alias = models.CharField(max_length=100, blank=True, null=True)

    @property
    def full_name(self):
        parts = []
        if self.title:
            parts.append(self.get_title_display())
        parts.append(self.first_name)
        parts.append(self.last_name)
        return " ".join(parts)

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=2, choices=pytz.country_names.items())
    founded_year = models.IntegerField()
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # books = models.ManyToOneField(Book, related_name='publisher')

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Series(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

class Note(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)

    