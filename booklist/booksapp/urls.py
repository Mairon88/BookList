from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import BookViewSet


book_list = BookViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('', views.list_of_book, name='list_of_books'),
    path('add_book_manually', views.add_book_manually, name='add_book_manually'),
    path('import_books', views.import_books, name='import_books'),
    path('<int:id>/', views.edit_book, name='edit_book'),
    path('api/', book_list, name='book-list'),




]