# Generated by Django 3.2.7 on 2021-10-02 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type_name', models.CharField(max_length=100)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.user')),
            ],
        ),
        migrations.CreateModel(
            name='healthService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.user')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField()),
                ('professionalID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional', to='features.user')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='features.user')),
            ],
        ),
    ]
