from django.db import models

# Create your models here.

class Info(models.Model):
    place = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    phoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.email
