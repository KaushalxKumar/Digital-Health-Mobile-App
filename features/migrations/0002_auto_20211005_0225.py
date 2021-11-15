# Generated by Django 3.2.7 on 2021-10-04 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='healthProfessional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usertype',
            name='userID',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='healthService',
        ),
        migrations.DeleteModel(
            name='userType',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='professionalID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.healthprofessional'),
        ),
    ]