# Generated by Django 4.1.3 on 2023-11-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmler', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
