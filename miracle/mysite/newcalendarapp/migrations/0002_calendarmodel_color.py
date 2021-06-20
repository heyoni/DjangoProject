# Generated by Django 3.1.3 on 2021-06-20 20:57

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newcalendarapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarmodel',
            name='color',
            field=colorfield.fields.ColorField(choices=[('#FF0000', 'red'), ('#FFA500', 'orange'), ('#FFFF00', 'yellow'), ('#34A223', 'green'), ('#0000FF', 'blue'), ('#00498C', 'navy'), ('#8B00FF', 'red'), ('#000000', 'black'), ('#FFFFFF', 'white')], default='#FFFFFF', max_length=18),
        ),
    ]