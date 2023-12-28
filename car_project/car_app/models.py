from django.db import models


class UserMaster(models.Model):
    ROLE_CHOICES = (
        (0, 'User'),
        (1, 'Admin'),
    )
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length = 10)
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()


class Booking(models.Model):
    user = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_booked = models.DateTimeField(auto_now_add=True)