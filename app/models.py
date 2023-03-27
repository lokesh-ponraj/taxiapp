from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    confpass = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Booking(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        origin = models.CharField(max_length=100, null=True)
        destination = models.CharField(max_length=100)
        location = models.CharField(max_length=50)
        pickup = models.TimeField(auto_now=False, auto_now_add=False)
        phone = models.CharField(max_length=12)

        def __str__(self) :
             return self.user.username
