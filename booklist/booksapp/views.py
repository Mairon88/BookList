from django.shortcuts import render, redirect, get_object_or_404
from .filters import BooksFilter
from .models import Book
from .forms import BookForm
from .functions import get_book_from_api
from rest_framework import viewsets
from .serializers import BookSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



def list_of_book(request):
    books_list = Book.objects.all()
    books_filter = BooksFilter(request.GET, queryset=books_list)

    if request.method == "POST" and request.POST.get('delete_items'):
        items_to_delete = request.POST.getlist('delete_items')
        Book.objects.filter(pk__in=items_to_delete).delete()
        return redirect('/')


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



# class BookViewSet(viewsets.ReadOnlyModelViewSet):
#
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BooksFilter

# @csrf_exempt
# def books_rest_api(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#
# @csrf_exempt
# def books_rest_api_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return JsonResponse(serializer.data)