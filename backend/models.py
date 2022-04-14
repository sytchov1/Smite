from django import forms
from django.db import models
from django.contrib.postgres.fields import ArrayField


'''ITEM_TYPES = [
    (1, 'Энчант'),
    (2, 'Оружие'),
    (3, 'Ювелирный камень'),
    (4, 'Броня'),
]'''

WEAPON_SUB_TYPES = [
    (0, 'Одноручный топор'),
    (1, 'Двуручный топор'),
    (2, 'Лук'),
    (3, 'Огнестрельное'),
    (4, 'Одноручное дробящее'),
    (5, 'Двуручное дробящее'),
    (6, 'Древковое'),
    (7, 'Одноручный меч'),
    (8, 'Двуручный меч'),
    (10, 'Посох'),
    (13, 'Кистевое'),
    (14, 'Разное'),
    (15, 'Кинжал'),
    (16, 'Метательное'),
    (18, 'Арбалет'),
    (19, 'Жезл'),
    (20, 'Удочка'),
]

ARMOR_SUB_TYPES = [
    (-8, 'Рубашка'),
    (-7, 'Гербовая накидка'),
    (-6, 'Спина'),
    (-5, 'Левая рука'),
    (-4, 'Аксессуар'),
    (-3, 'Ожерелье'),
    (-2, 'Кольцо'),
    (0, 'Разное'),
    (1, 'Ткань'),
    (2, 'Кожа'),
    (3, 'Кольчуга'),
    (4, 'Латы'),
    (6, 'Щит'),
    (7, 'Манускрипт'),
    (8, 'Идол'),
    (9, 'Тотем'),
]


class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
            'widget': forms.CheckboxSelectMultiple,
        }
        defaults.update(kwargs)
        return super(ArrayField, self).formfield(**defaults)

    def to_python(self, value):
        res = super().to_python(value)
        if isinstance(res, list):
            value = [self.base_field.to_python(val) for val in res]
        return value


class Item(models.Model):
    SOCKETS = [
        (0, 'Нет'),
        (1, 'Голова'),
        (2, 'Шея'),
        (3, 'Плечи'),
        (4, 'Рубашка'),
        (5, 'Грудь'),
        (6, 'Пояс'),
        (7, 'Ноги'),
        (8, 'Ступни'),
        (9, 'Запястья'),
        (10, 'Кисти рук'),
        (11, 'Палец'),
        (12, 'Аксессуар'),
        (13, 'Одноручное'),
        (14, 'Левая рука'),
        (15, 'Дальний бой'),
        (16, 'Спина'),
        (17, 'Двуручное'),
        (19, 'Гербовая накидка'),
        (21, 'Правая рука'),
        (22, 'Левая рука'),
        (23, 'Левая рука'),
        (28, 'Реликвия'),
    ]

    name = models.CharField('Название', max_length=255)
    quality = models.CharField('Качество', max_length=2)
    socket = models.IntegerField('Слот', choices=SOCKETS, default=0)
    html_tooltip = models.TextField('Всплывающее окно')
    icon = models.CharField('Иконка', max_length=63)
    stats = models.JSONField('Характеристики', null=True, default=None)

    
    class Meta:
        abstract = True
        ordering = ['name']


class Weapon(Item):
    subtype = models.IntegerField('Подтип', choices=WEAPON_SUB_TYPES)
    reqclass = models.IntegerField('Требуемый класс', null=True, default=None)
    uniq = models.BooleanField('Уникальный', default=False)

    class Meta:
        verbose_name = 'Оружие'
        verbose_name_plural = 'Оружие'


class Armor(Item):
    subtype = models.IntegerField('Подтип', choices=ARMOR_SUB_TYPES)
    reqclass = models.IntegerField('Требуемый класс', null=True, default=None)

    class Meta:
        verbose_name = 'Броня'
        verbose_name_plural = 'Броня'


class Gem(Item):
    uniq = models.BooleanField('Уникальный', default=False)

    class Meta:
        verbose_name = 'Самоцвет'
        verbose_name_plural = 'Самоцветы'


# В разработке
#class Enchant(Item):
#    pass


class WowClass(models.Model):
    name = models.CharField('Название', max_length=63, unique=True)
    armor_types = ChoiceArrayField(verbose_name='Доступная броня',
        base_field=models.IntegerField(
            choices=ARMOR_SUB_TYPES
        )
    )
    weapon_types = ChoiceArrayField(verbose_name='Доступное оружие',
        base_field=models.IntegerField(
            choices=WEAPON_SUB_TYPES
        )
    )
    icon = models.CharField('Иконка', max_length=63, default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'