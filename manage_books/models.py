from django.db import models

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
        ('hebrew', 'Hebrew'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    publication_date = models.DateField()
    pages = models.IntegerField()
    cover = models.CharField(max_length=20)
    language = models.CharField(max_length=20 )
    is_read = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
  
class Author(models.Model):
   
class Publisher(models.Model):
    
class Genre(models.Model):   

class series(models.Model):

class Topic(models.Model):

class category(models.Model):

class Note(models.Model):