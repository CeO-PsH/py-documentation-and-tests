# Generated by Django 4.1 on 2023-08-31 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
    ]
