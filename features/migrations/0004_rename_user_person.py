# Generated by Django 3.2.8 on 2021-11-22 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20211122_1813'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
    ]