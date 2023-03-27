from django.db import models


class Users(models.Model):
    user = models.CharField(
        verbose_name='id пользователя',
        max_length=255)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




class Category(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Review(models.Model):
    title = models.CharField(
        verbose_name='Имя пользователя',
        max_length=255
    )
    text = models.TextField(
        verbose_name='Описание отзыва'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'


class Channel(models.Model):
    logo = models.ImageField(
        verbose_name='Логотип',
        upload_to='channels_logo'
    )
    title = models.CharField(
        verbose_name='Название',
        max_length=255
    )
    text = models.TextField(
        verbose_name='Описание'
    )
    telegram_link = models.URLField(
        verbose_name='Ссылка на телеграмм канал',
        null=True
    )
    tgstat_link = models.URLField(
        verbose_name='Ссылка на тгстат',
        null=True
    )
    telemetr_link = models.URLField(
        verbose_name='Ссылка на телеметр',
        null=True
    )
    subscribes_count = models.IntegerField(
        verbose_name='Количество подписчиков',
        default=0
    )
    category = models.ForeignKey(
        Category,
        related_name='channels',
        on_delete=models.SET_NULL,
        null=True
    )


    CPM = models.IntegerField(
        verbose_name='CPM индикатор',
        default=0
    )

    ERR = models.IntegerField(
        verbose_name='ERR индикатор',
        default=0
    )

    coverage = models.IntegerField(
        verbose_name='индикатор охвата',
        default=0
    )

    reviews = models.ManyToManyField(
        Review,
        verbose_name='Отзывы',
        blank=True
    )

    woman = models.IntegerField(
        verbose_name='Женский%',
        default=0
    )

    man = models.IntegerField(
        verbose_name='Мужской%',
        default='0'
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        unique_together = ['title', 'category']
        verbose_name = 'Канал'
        verbose_name_plural = 'Канал'


class Country(models.Model):
    title = models.CharField(
        verbose_name='Гео',
        max_length=50
    )

    traffic_percentage = models.IntegerField(
        verbose_name='Трафик страны%',
        default="%"
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Трафик стран'
        verbose_name_plural = 'Трафик стран'


class Favorites(models.Model):
    user = models.ForeignKey(Users, related_name='favorite', on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
