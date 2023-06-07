from django.db import models

# Create your models here.
class Registration(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField(max_length=100)
    Phone_number=models.BigIntegerField()
    Password=models.CharField(max_length=100)
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    event = models.CharField(max_length=100)
    price = models.IntegerField()
    number_of_persons = models.IntegerField()
    totalprice=models.IntegerField()
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=254)
