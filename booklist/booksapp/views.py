from django.shortcuts import render, redirect, get_object_or_404
from .filters import BooksFilter
from .models import Book
from .forms import BookForm
from .functions import get_book_from_api

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

def import_books(request):
    keyword = ''
    if request.method == 'GET' and request.GET.get('results'):
        keyword = request.GET.get('results')
        if keyword:
            books_info = get_book_from_api(keyword)
            for info in books_info:
                book_obj = Book(title=info['title'], author=info['authors'], year_of_publication=info['date'],
                                other_identifier=info['other_id'], isbn13=info['isbn13'], isbn10=info['isbn10'],
                                pages=info['pages'], language=info['language'], link=info['img'])
                book_obj.save()
        return redirect('/')



    return render(request, 'import_books.html',
                  {'keyword': keyword})