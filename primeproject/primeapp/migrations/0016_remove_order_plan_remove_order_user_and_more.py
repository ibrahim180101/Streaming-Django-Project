# Generated by Django 5.0.6 on 2024-07-08 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primeapp', '0015_subscriptionplan_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='SubscriptionPlan',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]