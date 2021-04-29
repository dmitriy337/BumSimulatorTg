from django.db import models
import datetime
# Create your models here.


class StatusOfBum(models.TextChoices):
    Bum_0 = ('0','Бомж')
    Bum_1 = ('1','Младший бомж')
    Bum_2 = ('2','Нищеброд')
    Bum_3 = ('3','Босяк')
    Bum_4 = ('4','Старший бомж')
    Bum_5 = ('5','Искатель счастья')


class Eat_activity(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of eat')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of eat')
    price = models.IntegerField(default=0, null=False, verbose_name='Price of eat')
    howMuchHealthMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding health')
    howMuchHealthMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding health')
    howMuchEatMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding eat')
    howMuchEatMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding eat')
    howMuchHappyMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding happy')
    howMuchHappyMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding happy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Действия для еды'
        verbose_name = 'Действие для еды'
        ordering = ['price']


class Happy_activity(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of Happy')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of Happy')
    price = models.IntegerField(default=0, null=False, verbose_name='Price of Happy')
    howMuchHealthMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding health')
    howMuchHealthMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding health')
    howMuchEatMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding eat')
    howMuchEatMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding eat')
    howMuchHappyMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding happy')
    howMuchHappyMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding happy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Действия для счастья'
        verbose_name = 'Действиe для счастья'
        ordering = ['price']



class Health_activity(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of Health')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of Health')
    price = models.IntegerField(default=0, null=False, verbose_name='Price of Health')
    howMuchHealthMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding health')
    howMuchHealthMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding health')
    howMuchEatMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding eat')
    howMuchEatMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding eat')
    howMuchHappyMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding happy')
    howMuchHappyMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding happy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Действия для здоровья'
        verbose_name = 'Действиe для здоровья'
        ordering = ['price']


class PersonageWorks(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of PersonageWork')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of PersonageWork')
    HowMuchEarningsMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding money')
    HowMuchEarningsMax = models.IntegerField(default=0, null=False, verbose_name='Max count of adding money')
    HowMuchEarningsItemsMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding Items')
    HowMuchEarningsItemsMax = models.IntegerField(default=0, null=False, verbose_name='Max count of adding Items')
    howMuchHealthMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding health')
    howMuchHealthMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding health')
    howMuchEatMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding eat')
    howMuchEatMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding eat')
    howMuchHappyMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding happy')
    howMuchHappyMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding happy')
    howMuchRatingMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding rating')
    howMuchRatingMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding rating')
    unlockRating = models.IntegerField(null=False, default=0, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Работы персонажа'
        verbose_name = 'Работа персонажа'
        ordering = ['HowMuchEarningsMin']



class NormalWorks(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of NormalWork')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of NormalWork')
    HowMuchEarningsMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding money')
    HowMuchEarningsMax = models.IntegerField(default=0, null=False, verbose_name='Max count of adding money')
    howMuchHealthMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding health')
    howMuchHealthMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding health')
    howMuchEatMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding eat')
    howMuchEatMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding eat')
    howMuchHappyMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding happy')
    howMuchHappyMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding happy')
    howMuchRatingMin = models.IntegerField(default=0, null=False, verbose_name='Min count of adding rating')
    howMuchRatingMax = models.IntegerField(default=1, null=False, verbose_name='Max count of adding rating')
    unlockRating = models.IntegerField(null=False, default=0, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Нормальные работы'
        verbose_name = 'Нормальная работа'
        ordering = ['HowMuchEarningsMin']



class Learning_params(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of Learning')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of Learning')
    price = models.IntegerField(default=0, null=False, verbose_name='Price')
    howMuchRating = models.IntegerField(default=0, null=False, verbose_name='how Much Rating')
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Обучение'
        verbose_name = 'Обучение'
        ordering = ['price']



class Houses(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of House')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of House')
    price = models.IntegerField(default=0, null=False, verbose_name='Price')
    howMuchRating = models.IntegerField(default=0, null=False, verbose_name='Count of adding rating')
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Дома'
        verbose_name = 'Дом'
        ordering = ['price']


class Transports(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of Transport')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of Transport')
    price = models.IntegerField(default=0, null=False, verbose_name='Price')
    howMuchRating = models.IntegerField(default=0, null=False, verbose_name='Count of adding rating')
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Транспорты'
        verbose_name = 'Транспорт'
        ordering = ['price']


class Personage(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(default=20, null=False, verbose_name='Age')
    money = models.IntegerField(default=500, verbose_name='Money')
    items = models.IntegerField(default=10, verbose_name='Count of bottles')
    rating = models.IntegerField(default=0, verbose_name='Rating')
    status = models.CharField(
        max_length=2,
        choices=StatusOfBum.choices,
        default=StatusOfBum.Bum_0,
    )
    date = models.DateTimeField(auto_now_add=True, blank=True)
    dateToTrack = models.DateTimeField(auto_now_add=True, blank=True)
    happy_level = models.IntegerField(default=100, null=False, verbose_name='Happy level')
    eat_level = models.IntegerField(default=100, null=False, verbose_name='Happy level')
    health_level = models.IntegerField(default=100, null=False, verbose_name='Happy level')
    house = models.ForeignKey(Houses, null=True, blank=True, on_delete=models.PROTECT
                              , verbose_name='Personage house')
    transport = models.ForeignKey(Transports, null=True, blank=True, on_delete=models.PROTECT
                                  , verbose_name='Personage transport')

    def __str__(self):
        return f"{str(self.id)} 💸:{str(self.money)}  ❤:{str(self.health_level)} 🍆:{str(self.eat_level)} 😁:{str(self.happy_level)}"

    class Meta:
        verbose_name_plural = 'Персонажи'
        verbose_name = 'Персонаж'
        ordering = ['money']

    @classmethod
    def get_new(cls):
        return cls.objects.create().id


class User(models.Model):
    Id = models.IntegerField(unique=True, null=False)
    Username = models.TextField(max_length=100, null=True, blank=True, verbose_name='User Name')
    Firstname = models.TextField(max_length=100, null=True, blank=True, verbose_name='First Name')
    LastName = models.TextField(max_length=100, null=True, blank=True, verbose_name='Last Name')
    Character = models.OneToOneField(Personage,
        on_delete = models.CASCADE,
        primary_key = True,
        default=Personage.get_new)

    def __str__(self):
        if self.Username != None and self.Firstname:
            return ("@"+str(self.Username)+'   '+str(self.Firstname))
        if self.Username != None and self.LastName:
            return ("@"+str(self.Username)+'    '+str(self.LastName))
        if self.Firstname != None and self.LastName:
            return (str(self.Firstname)+' '+str(self.LastName))
        return str(self.Id)

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['Username']