# Generated by Django 3.1.3 on 2021-06-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rutineapp', '0006_auto_20210616_1431'),
        ('newcalendarapp', '0003_auto_20210613_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color1', to='rutineapp.color'),
        ),
    ]
