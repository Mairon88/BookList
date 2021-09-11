from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','year_of_publication','isbn10', 'isbn13', 'other_identifier', 'pages']
