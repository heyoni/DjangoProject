# Generated by Django 3.1.3 on 2021-02-26 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jusik', '0004_jusik_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jusik_list',
            name='buy_amount',
        ),
        migrations.RemoveField(
            model_name='jusik_list',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='jusik_list',
            name='sell_amount',
        ),
    ]
