# Generated by Django 2.2.4 on 2021-06-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animes',
            name='pic_bg',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='animes',
            name='pic_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='animes',
            name='trailer_url',
            field=models.URLField(),
        ),
    ]
