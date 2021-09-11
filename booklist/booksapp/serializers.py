from rest_framework import serializers
from .models import Book
from django.core.validators import RegexValidator, MinValueValidator


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year_of_publication', 'isbn13', 'isbn10', 'other_identifier', 'pages', 'link',
                 'language']


    def create(self, validated_data):
        return Book.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('title', instance.title)
        instance.year_of_publication = validated_data.get('year_of_publication', instance.year_of_publication)
        instance.isbn13 = validated_data.get('isbn13', instance.isbn13)
        instance.isbn10 = validated_data.get('isbn10', instance.isbn10)
        instance.other_identifier = validated_data.get('other_identifier', instance.other_identifier)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.link = validated_data.get('link', instance.link)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance
