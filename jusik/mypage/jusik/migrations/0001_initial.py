# Generated by Django 3.1.3 on 2021-02-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jusik_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateTimeField()),
                ('stock_name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('buy_price', models.IntegerField()),
                ('buy_amount', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('sell_amount', models.IntegerField()),
                ('profit', models.IntegerField()),
            ],
        ),
    ]