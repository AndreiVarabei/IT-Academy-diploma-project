# Generated by Django 4.0.3 on 2022-03-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_alter_companies_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
