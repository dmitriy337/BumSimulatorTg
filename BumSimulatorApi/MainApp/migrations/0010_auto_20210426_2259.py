# Generated by Django 3.2 on 2021-04-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_personage_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalworks',
            name='howMuchRatingMax',
            field=models.IntegerField(default=1, verbose_name='Max count of adding rating'),
        ),
        migrations.AddField(
            model_name='normalworks',
            name='howMuchRatingMin',
            field=models.IntegerField(default=0, verbose_name='Min count of adding rating'),
        ),
        migrations.AddField(
            model_name='personageworks',
            name='howMuchRatingMax',
            field=models.IntegerField(default=1, verbose_name='Max count of adding rating'),
        ),
        migrations.AddField(
            model_name='personageworks',
            name='howMuchRatingMin',
            field=models.IntegerField(default=0, verbose_name='Min count of adding rating'),
        ),
    ]
