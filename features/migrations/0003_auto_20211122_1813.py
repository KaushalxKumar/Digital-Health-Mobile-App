# Generated by Django 3.2.8 on 2021-11-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_auto_20211005_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='healthProfessional',
        ),
    ]
