# Generated by Django 4.0.3 on 2022-03-28 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('ticker', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('change', models.CharField(max_length=50)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
