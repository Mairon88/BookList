from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import list_of_book, add_book_manually, import_books
from .models import Book
from .functions import get_book_from_api
from .forms import BookForm


class BooksappTests(TestCase):
    # ============= test URLs ================
    def test_urls_list_of_book(self):
        url = reverse('list_of_book')
        self.assertEqual(resolve(url).func, list_of_book)

    def test_urls_add_book_manually(self):
        url = reverse('add_book_manually')
        self.assertEqual(resolve(url).func, add_book_manually)

    def test_urls_import_books(self):
        url = reverse('import_books')
        self.assertEqual(resolve(url).func, import_books)

    def test_get_absolute_urls_edit_book(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/1/')

    # ============= test Views ================

    def test_view_list_of_book(self):

        client = Client()
        response = client.get(reverse('list_of_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booklist.html')

    def test_view_add_book_manually(self):
        client = Client()
        response = client.get(reverse('add_book_manually'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_book_manually.html')

    def test_view_import_books(self):
        client = Client()
        response = client.get(reverse('import_books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'import_books.html')
    #

    def test_view_edit_book(self):
        client = Client()
        book = Book.objects.get(id=1)
        response = client.get(f'/{book.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_book.html')

    # ============= test Models  ================
    def setUp(self):
        link = "https://tipsmake.com/data1/thumbs/how-to-extract-img-files-in-windows-10-thumb-bzxI4IDgg.jpg"
        self.book = Book.objects.create(title='title_1', author='author_1', year_of_publication='2021',
                                        isbn13=1234567890123, pages=200, link=link, language='pl')
        keyword = 'Sonic'
        self.function = get_book_from_api(keyword)

    def test_book_as_title(self):
        self.assertEqual(str(self.book), 'title_1')

    def test_book_isbn10_is_empty(self):
        self.assertEqual(self.book.isbn10, None)

    def test_book_in_not_null(self):
        self.assertNotEqual(self.book, None)

    # ============= test Functions ================

    def test_func_first_element(self):
        element_of_list = {'title': "Where's Sonic?.", 'authors': 'LADYBIRD BOOKS, Penguin Books, '
                                                                  'Limited, Penguin Group Australia',
                           'date': '1994', 'other_id': None, 'isbn10': '0721434363', 'isbn13': '9780721434360',
                           'pages': 32, 'language': 'en',
                           'img': 'http://books.google.com/books/content?id=m5uDAAAACAAJ&printsec=frontcover&img=1&'
                                  'zoom=1&source=gbs_api'}
        self.assertEqual(self.function[0], element_of_list)

    # ============= test Forms  ===================
    def test_form_is_valid_isbn13(self):
        form = BookForm(data={
            'title': "Test",
            'author': "Testowy",
            'year_of_publication': 2000,
            'language': 'en',
            'isbn13': 1234567890123,
        })
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid_isbn13(self):
        form = BookForm(data={
            'title': "Test",
            'author': "Testowy",
            'year_of_publication': 2000,
            'language': 'en',
            'isbn13': 12345923,
        })
        self.assertFalse(form.is_valid())

    def test_form_is_valid_isbn10(self):
        form = BookForm(data={
            'title': "Test",
            'author': "Testowy",
            'year_of_publication': 2000,
            'language': 'en',
            'isbn10': 1234560789,
        })
        self.assertTrue(form.is_valid())

    def test_form_is_not_valid_isbn10(self):
        form = BookForm(data={
            'title': "Test",
            'author': "Testowy",
            'year_of_publication': 2000,
            'language': 'en',
            'isbn10': 1235,
        })
        self.assertFalse(form.is_valid())

    def test_form_is_not_valid_pages(self):
        form = BookForm(data={
            'title': "Test",
            'author': "Testowy",
            'year_of_publication': 2000,
            'language': 'en',
            'pages': 2,
        })
        self.assertFalse(form.is_valid())

    def test_form_is_valid_pages(self):
        form = BookForm(data={
            'title': "Test",
            'author': "Testowy",
            'year_of_publication': 2000,
            'language': 'en',
            'pages': 300,
        })
        self.assertTrue(form.is_valid())
