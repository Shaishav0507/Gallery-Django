# Generated by Django 4.0.6 on 2022-07-22 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_category_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
    ]
