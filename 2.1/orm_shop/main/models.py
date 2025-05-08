from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    date_of_birth = models.DateField('Дата рождения')
    phone_number = models.CharField('Номер телефона', max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        

GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    model = models.CharField('Модель', max_length=100)
    year = models.PositiveSmallIntegerField('Год выпуска')
    color = models.CharField('Цвет', max_length=20)
    mileage = models.PositiveSmallIntegerField('Пробег', default=0)
    volume = models.FloatField('Объём двигателя', null=True)
    body_type = models.CharField('Тип кузова', max_length=20, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField('Привод', max_length=10, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField('Коробка передач', max_length=10, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField('Тип толива', max_length=10, choices=FUEL_TYPE_CHOICES)
    price = models.PositiveIntegerField('Цена', null=True)
    image = models.ImageField('Изображение', upload_to='cars/')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Автомбобиль'
        verbose_name_plural = 'Автомобили'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль', related_name='sales')
    created_at = models.DateTimeField('Дата/время продажи', auto_now_add=True)

    def __str__(self):
        return f'{self.client} - {self.car}'
    
    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
