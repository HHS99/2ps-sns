# Generated by Django 3.2.5 on 2021-12-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsApp', '0005_rename_board_id_commentmodel_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]