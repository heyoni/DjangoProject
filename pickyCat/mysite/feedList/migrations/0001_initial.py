# Generated by Django 3.1.3 on 2021-10-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='사료 이름')),
                ('crude_protein', models.IntegerField(blank=True)),
                ('crude_Fat', models.IntegerField(blank=True)),
                ('phosphorus', models.IntegerField(blank=True)),
                ('palatability', models.CharField(choices=[('LIKE', '좋아!'), ('DISLIKE', '그냥 그래..'), ('HATE', '싫어!')], max_length=7)),
            ],
        ),
    ]