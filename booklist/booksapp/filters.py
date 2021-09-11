from .models import Book
import django_filters


class BooksFilter(django_filters.FilterSet):
    YEAR_CHOICES = list(zip(range(1900, 2022), range(1900, 2022)))

    year_of_publication__gte = django_filters.ChoiceFilter(field_name='year_of_publication', choices=YEAR_CHOICES,
                                                           lookup_expr='gte')
    year_of_publication__lte = django_filters.ChoiceFilter(field_name='year_of_publication', choices=YEAR_CHOICES,
                                                           lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author', 'language']
