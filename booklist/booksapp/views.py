from django.shortcuts import render
from .filters import BooksFilter
from .models import Book

# Create your views here.
def list_of_book(request):
    books_list = Book.objects.all()
    books_filter = BooksFilter(request.GET, queryset=books_list)

    return render(request, 'booklist.html',
                  {'filter': books_filter})