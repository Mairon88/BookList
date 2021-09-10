from django.shortcuts import render, redirect, get_object_or_404
from .filters import BooksFilter
from .models import Book
from .forms import BookForm

# Create your views here.


def list_of_book(request):
    books_list = Book.objects.all()
    books_filter = BooksFilter(request.GET, queryset=books_list)

    return render(request, 'booklist.html',
                  {'filter': books_filter})


def add_book_manually(request):
    if request.method == 'POST':
        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            new_book = book_form.save(commit=False)
            new_book.save()

            return redirect('/')

    else:
        book_form = BookForm()
    return render(request, 'add_book_manually.html',
                  {'book_form': book_form})


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book_form = BookForm(request.POST, request.FILES, instance=book)
        if book_form.is_valid():
            book_form.save()
            return redirect('/')

    else:
        book_form = BookForm(instance=book)

    return render(request, 'edit_book.html',
                  {'book_form': book_form})
