# Generated by Django 5.0.6 on 2024-07-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primeapp', '0007_delete_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainsectionMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.IntegerField(choices=[(1, 'Action and Adventure'), (2, 'Comedy'), (3, 'Drama'), (4, 'Horror'), (5, 'Romance'), (7, 'Kids'), (8, 'Mystery and Thrillers')])),
                ('description', models.TextField(max_length=700)),
                ('cover_image', models.ImageField(upload_to='media/')),
                ('video', models.FileField(upload_to='media/videos/')),
                ('imdb', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('time', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
