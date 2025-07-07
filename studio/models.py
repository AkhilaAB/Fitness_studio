from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=100)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email
    
class FitnessClass(models.Model):
    name=models.CharField(max_length=100)
    date_time=models.DateTimeField()
    instructor=models.CharField(max_length=100)
    total_slots=models.IntegerField()
    available_slots=models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.date_time}"
    
class Booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fitness_class=models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    booking_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.fitness_class.name} - {self.booking_date}"
