# Generated by Django 4.0.3 on 2022-03-31 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tikers',
        ),
        migrations.CreateModel(
            name='tikers_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tikers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tikers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
