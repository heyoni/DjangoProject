# Generated by Django 3.1.3 on 2021-06-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newcalendarapp', '0002_auto_20210611_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.CharField(default='red', max_length=150, null=True),
        ),
    ]
