# Generated by Django 4.0.3 on 2022-03-31 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_remove_tikers_profile_tikers_tikers_profile_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tikers_profile',
            name='ticker',
            field=models.CharField(default=None, max_length=10, unique=True),
        ),
    ]