from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year_of_publication', 'isbn10', 'isbn13', 'other_identifier', 'pages', 'link',
                  'language')
