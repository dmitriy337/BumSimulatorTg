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
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name


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
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name


class Learning_params(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of Learning')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of Learning')
    price = models.IntegerField(default=0, null=False, verbose_name='Min count of adding money')
    howMuchRating = models.IntegerField(default=0, null=False, verbose_name='Count of adding rating')
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name


class Houses(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of House')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of House')
    price = models.IntegerField(default=0, null=False, verbose_name='Price')
    howMuchRating = models.IntegerField(default=0, null=False, verbose_name='Count of adding rating')
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name


class Transports(models.Model):
    name = models.TextField(max_length=100, null=True, verbose_name='Name of Transport')
    description = models.TextField(max_length=100, null=True, verbose_name='Description of Transport')
    price = models.IntegerField(default=0, null=False, verbose_name='Price')
    howMuchRating = models.IntegerField(default=0, null=False, verbose_name='Count of adding rating')
    unlockRating = models.IntegerField(null=False, verbose_name='Min rating for unlock')

    def __str__(self):
        return self.name


class Personage(models.Model):
    age = models.IntegerField(default=20, null=False, verbose_name='Age')
    money = models.IntegerField(default=500, verbose_name='Money')
    items = models.IntegerField(default=10, verbose_name='Count of bottles')
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
    house = models.ForeignKey(Houses, null=True ,blank=True, on_delete=models.PROTECT
                              , verbose_name='Personage house')
    transport = models.ForeignKey(Transports, null=True, blank=True, on_delete=models.PROTECT
                                  , verbose_name='Personage transport')

    def __str__(self):
        return str(self.id)


class User(models.Model):
    Id = models.IntegerField(unique=True, null=False)
    Username = models.TextField(max_length=100, null=True, verbose_name='User Name')
    Firstname = models.TextField(max_length=100, null=True, verbose_name='First Name')
    LastName = models.TextField(max_length=100, null=True, verbose_name='Last Name')
    Character = models.OneToOneField(Personage, on_delete=models.CASCADE)

    def __str__(self):
        return  ('@' +self.Username + ' ' + self.Firstname)