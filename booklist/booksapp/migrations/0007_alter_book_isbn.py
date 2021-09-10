# Generated by Django 3.2.7 on 2021-09-10 12:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0006_auto_20210910_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(code='nomatch', message='Correct format is XXX-XX-XXXXX-XX-X, where X is a number from 0 to 9', regex='\\d{13}')]),
        ),
    ]
