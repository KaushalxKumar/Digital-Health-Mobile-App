# Generated by Django 3.2.8 on 2021-12-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_alter_person_on_demand'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
