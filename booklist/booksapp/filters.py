from .models import Book
import django_filters

class BooksFilter(django_filters.FilterSet):
    YEAR_CHOICES = list(zip(range(1900, 2022), range(1900, 2022)))

    year_of_publication__gt = django_filters.ChoiceFilter(field_name='year_of_publication', choices=YEAR_CHOICES, lookup_expr='gt')
    year_of_publication__lt = django_filters.ChoiceFilter(field_name='year_of_publication', choices=YEAR_CHOICES, lookup_expr='lt')
    class Meta:
        model = Book
        fields = ['title', 'author', 'language']

