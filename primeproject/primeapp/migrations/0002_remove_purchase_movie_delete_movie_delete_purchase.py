# Generated by Django 5.0.6 on 2024-07-03 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
