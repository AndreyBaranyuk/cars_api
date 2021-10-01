from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Car(models.Model):
    vin = models.CharField(max_length=64, unique=True)
    color = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэтчбэк'),
        (3, 'Универсал'),
        (4, 'Купе')
    )
    car_type = models.IntegerField(choices=CAR_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
