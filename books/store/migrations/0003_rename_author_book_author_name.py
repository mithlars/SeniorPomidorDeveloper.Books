# Generated by Django 4.2.4 on 2023-09-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_name',
        ),
    ]
