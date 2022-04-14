# Generated by Django 4.0.1 on 2022-03-20 15:26

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('quality', models.CharField(max_length=2, verbose_name='Качество')),
                ('socket', models.IntegerField(choices=[(0, 'Нет'), (1, 'Голова'), (2, 'Шея'), (3, 'Плечи'), (4, 'Рубашка'), (5, 'Грудь'), (6, 'Пояс'), (7, 'Ноги'), (8, 'Ступни'), (9, 'Запястья'), (10, 'Кисти рук'), (11, 'Палец'), (12, 'Аксессуар'), (13, 'Одноручное'), (14, 'Левая рука'), (15, 'Дальний бой'), (16, 'Спина'), (17, 'Двуручное'), (19, 'Гербовая накидка'), (21, 'Правая рука'), (22, 'Левая рука'), (23, 'Левая рука'), (28, 'Реликвия')], default=0, verbose_name='Слот')),
                ('html_tooltip', models.TextField(verbose_name='Всплывающее окно')),
                ('icon', models.CharField(max_length=63, verbose_name='Иконка')),
                ('stats', models.JSONField(default=None, null=True, verbose_name='Характеристики')),
                ('subtype', models.IntegerField(choices=[(-8, 'Рубашка'), (-7, 'Гербовая накидка'), (-6, 'Спина'), (-5, 'Левая рука'), (-4, 'Аксессуар'), (-3, 'Ожерелье'), (-2, 'Кольцо'), (0, 'Разное'), (1, 'Ткань'), (2, 'Кожа'), (3, 'Кольчуга'), (4, 'Латы'), (6, 'Щит'), (7, 'Манускрипт'), (8, 'Идол'), (9, 'Тотем')], verbose_name='Подтип')),
                ('reqclass', models.IntegerField(default=None, null=True, verbose_name='Требуемый класс')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('quality', models.CharField(max_length=2, verbose_name='Качество')),
                ('socket', models.IntegerField(choices=[(0, 'Нет'), (1, 'Голова'), (2, 'Шея'), (3, 'Плечи'), (4, 'Рубашка'), (5, 'Грудь'), (6, 'Пояс'), (7, 'Ноги'), (8, 'Ступни'), (9, 'Запястья'), (10, 'Кисти рук'), (11, 'Палец'), (12, 'Аксессуар'), (13, 'Одноручное'), (14, 'Левая рука'), (15, 'Дальний бой'), (16, 'Спина'), (17, 'Двуручное'), (19, 'Гербовая накидка'), (21, 'Правая рука'), (22, 'Левая рука'), (23, 'Левая рука'), (28, 'Реликвия')], default=0, verbose_name='Слот')),
                ('html_tooltip', models.TextField(verbose_name='Всплывающее окно')),
                ('icon', models.CharField(max_length=63, verbose_name='Иконка')),
                ('stats', models.JSONField(default=None, null=True, verbose_name='Характеристики')),
                ('uniq', models.BooleanField(default=False, verbose_name='Уникальный')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('quality', models.CharField(max_length=2, verbose_name='Качество')),
                ('socket', models.IntegerField(choices=[(0, 'Нет'), (1, 'Голова'), (2, 'Шея'), (3, 'Плечи'), (4, 'Рубашка'), (5, 'Грудь'), (6, 'Пояс'), (7, 'Ноги'), (8, 'Ступни'), (9, 'Запястья'), (10, 'Кисти рук'), (11, 'Палец'), (12, 'Аксессуар'), (13, 'Одноручное'), (14, 'Левая рука'), (15, 'Дальний бой'), (16, 'Спина'), (17, 'Двуручное'), (19, 'Гербовая накидка'), (21, 'Правая рука'), (22, 'Левая рука'), (23, 'Левая рука'), (28, 'Реликвия')], default=0, verbose_name='Слот')),
                ('html_tooltip', models.TextField(verbose_name='Всплывающее окно')),
                ('icon', models.CharField(max_length=63, verbose_name='Иконка')),
                ('stats', models.JSONField(default=None, null=True, verbose_name='Характеристики')),
                ('subtype', models.IntegerField(choices=[(0, 'Одноручный топор'), (1, 'Двуручный топор'), (2, 'Лук'), (3, 'Огнестрельное'), (4, 'Одноручное дробящее'), (5, 'Двуручное дробящее'), (6, 'Древковое'), (7, 'Одноручный меч'), (8, 'Двуручный меч'), (10, 'Посох'), (13, 'Кистевое'), (14, 'Разное'), (15, 'Кинжал'), (16, 'Метательное'), (18, 'Арбалет'), (19, 'Жезл'), (20, 'Удочка')], verbose_name='Подтип')),
                ('reqclass', models.IntegerField(default=None, null=True, verbose_name='Требуемый класс')),
                ('uniq', models.BooleanField(default=False, verbose_name='Уникальный')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WowClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True, verbose_name='Название')),
                ('armor_types', backend.models.ChoiceArrayField(base_field=models.IntegerField(choices=[(-8, 'Рубашка'), (-7, 'Гербовая накидка'), (-6, 'Спина'), (-5, 'Левая рука'), (-4, 'Аксессуар'), (-3, 'Ожерелье'), (-2, 'Кольцо'), (0, 'Разное'), (1, 'Ткань'), (2, 'Кожа'), (3, 'Кольчуга'), (4, 'Латы'), (6, 'Щит'), (7, 'Манускрипт'), (8, 'Идол'), (9, 'Тотем')]), size=None, verbose_name='Доступная броня')),
                ('weapon_types', backend.models.ChoiceArrayField(base_field=models.IntegerField(choices=[(0, 'Одноручный топор'), (1, 'Двуручный топор'), (2, 'Лук'), (3, 'Огнестрельное'), (4, 'Одноручное дробящее'), (5, 'Двуручное дробящее'), (6, 'Древковое'), (7, 'Одноручный меч'), (8, 'Двуручный меч'), (10, 'Посох'), (13, 'Кистевое'), (14, 'Разное'), (15, 'Кинжал'), (16, 'Метательное'), (18, 'Арбалет'), (19, 'Жезл'), (20, 'Удочка')]), size=None, verbose_name='Доступное оружие')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'ordering': ['name'],
            },
        ),
    ]
