# Generated by Django 4.1.7 on 2023-03-25 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='trending',
        ),
    ]
