# Generated by Django 3.2 on 2021-04-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_personage_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eat_activity',
            options={'ordering': ['price'], 'verbose_name': 'Действие для еды', 'verbose_name_plural': 'Действия для еды'},
        ),
        migrations.AlterModelOptions(
            name='happy_activity',
            options={'ordering': ['price'], 'verbose_name': 'Действиe для счастья', 'verbose_name_plural': 'Действия для счастья'},
        ),
        migrations.AlterModelOptions(
            name='health_activity',
            options={'ordering': ['price'], 'verbose_name': 'Действиe для здоровья', 'verbose_name_plural': 'Действия для здоровья'},
        ),
        migrations.AlterModelOptions(
            name='houses',
            options={'ordering': ['price'], 'verbose_name': 'Дом', 'verbose_name_plural': 'Дома'},
        ),
        migrations.AlterModelOptions(
            name='learning_params',
            options={'ordering': ['price'], 'verbose_name': 'Обучение', 'verbose_name_plural': 'Обучение'},
        ),
        migrations.AlterModelOptions(
            name='normalworks',
            options={'ordering': ['HowMuchEarningsMin'], 'verbose_name': 'Нормальная работа', 'verbose_name_plural': 'Нормальные работы'},
        ),
        migrations.AlterModelOptions(
            name='personage',
            options={'ordering': ['money'], 'verbose_name': 'Персонаж', 'verbose_name_plural': 'Персонажи'},
        ),
        migrations.AlterModelOptions(
            name='personageworks',
            options={'ordering': ['HowMuchEarningsMin'], 'verbose_name': 'Работа персонажа', 'verbose_name_plural': 'Работы персонажа'},
        ),
        migrations.AlterModelOptions(
            name='transports',
            options={'ordering': ['price'], 'verbose_name': 'Транспорт', 'verbose_name_plural': 'Транспорты'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['Username'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='learning_params',
            name='howMuchRating',
            field=models.IntegerField(default=0, verbose_name='how Much Rating'),
        ),
        migrations.AlterField(
            model_name='learning_params',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='age',
            field=models.IntegerField(default=20, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='personage',
            name='dateToTrack',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='personage',
            name='eat_level',
            field=models.IntegerField(default=100, verbose_name='Happy level'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='happy_level',
            field=models.IntegerField(default=100, verbose_name='Happy level'),
        ),
        migrations.AlterField(
            model_name='personage',
            name='health_level',
            field=models.IntegerField(default=100, verbose_name='Happy level'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Character',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='MainApp.personage'),
        ),
    ]
