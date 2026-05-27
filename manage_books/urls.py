from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('publishers/', views.publishers, name='publishers'),
    path('publisher/<int:publisher_id>/', views.publisher, name='publisher'),
    path('series/', views.series_list, name='series_list'),
    path('series/<int:series_id>/', views.series, name='series'),
    path('notes/', views.notes, name='notes'),
    path('note/<int:note_id>/', views.note, name='note'),
]