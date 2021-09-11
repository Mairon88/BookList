from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Book(models.Model):

    YEAR_CHOICE = list(zip(range(1900, 2022), range(1900, 2022)))

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    year_of_publication = models.IntegerField(choices=YEAR_CHOICE)
    isbn13 = models.CharField(max_length=13, validators=[RegexValidator(regex=r'\d{13}',
                            message='Please enter thirteen numbers from 0 to 9',code='nomatch')], null=True, blank=True)
    isbn10 = models.CharField(max_length=13, validators=[RegexValidator(regex=r'\d{10}',
                            message='Please enter ten numbers from 0 to 9',code='nomatch')], null=True, blank=True)
    other_identifier = models.CharField(max_length=30, null=True, blank=True)
    pages = models.IntegerField(validators=[MinValueValidator(5)], null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=20, default='en')


    def get_absolute_url(self):
        return reverse('edit_book', args=[self.id])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
