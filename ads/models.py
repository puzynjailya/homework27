from django.db import models


class Location(models.Model):
    id = models.AutoField(editable=False, unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=200, blank=False)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Локации'


class Category(models.Model):
    id = models.AutoField(editable=False, unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class User(models.Model):
    ROLES = [
        ('admin','Администратор ОПГ'),
        ('member', 'Участиник ОПГ'),
        ('moderator', 'Смотрящий за ОПГ'),
    ]
    id = models.AutoField(editable=False, unique=True, primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=75, blank=False)
    username = models.CharField(max_length=50, unique=True, blank=False)
    password = models.CharField(max_length=50, blank=False)
    role = models.CharField(max_length=9, choices=ROLES, blank=False)
    age = models.SmallIntegerField(blank=False)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Advertisement(models.Model):
    id = models.AutoField(editable=False, unique=True, primary_key=True, auto_created=True)
    name = models.CharField(max_length=150, null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=False)
    description = models.CharField(max_length=3000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


