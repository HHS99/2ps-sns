# Generated by Django 3.2.5 on 2021-12-04 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snsApp', '0004_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='board_id',
            new_name='board',
        ),
    ]
