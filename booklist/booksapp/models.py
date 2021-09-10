from django.core.validators import RegexValidator, MinValueValidator
from django.db import models


class Book(models.Model):
    YEAR_CHOICE = list(zip(map(str, range(1900, 2022)), map(str, range(1900, 2022))))

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    year_of_publication = models.CharField(max_length=4, choices=YEAR_CHOICE)
    isbn = models.CharField(max_length=17, validators=[RegexValidator(regex=r'\d{13}',
                            message='Please enter thirteen numbers from 0 to 9',code='nomatch')])
                            #\d\d\d-\d\d-\d\d\d\d\d-\d\d-\d regex with separated numbers
    pages = models.IntegerField(validators=[MinValueValidator(5)])
    link = models.URLField(max_length=200, null=True)
    language = models.CharField(max_length=20, default='English')

    def __str__(self):
        return self.title
