# Generated by Django 4.0.3 on 2022-03-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_rename_campanies_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='price_to_earn',
            field=models.CharField(default='10', max_length=50),
        ),
        migrations.AddField(
            model_name='companies',
            name='raiting',
            field=models.TextField(default='Неизвестно', max_length=250),
        ),
    ]
