# Generated by Django 5.0.6 on 2024-07-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeapp', '0013_rename_category_mainsectionseries_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsectionseries',
            name='genre',
            field=models.IntegerField(choices=[(1, 'Award-Winning Tv Shows'), (2, 'Epic worlds'), (3, 'Exciting Tv shows'), (4, 'Marvel Tv shows')]),
        ),
    ]