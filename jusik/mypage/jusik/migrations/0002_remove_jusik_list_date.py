# Generated by Django 3.1.3 on 2021-02-26 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jusik', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jusik_list',
            name='date',
        ),
    ]