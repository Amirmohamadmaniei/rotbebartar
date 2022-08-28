from django.db import models
from user.models import CustomUser


# class Consultant(CustomUser):
#     records = models.CharField(max_length=50, null=True, blank=True)
#     image = models.ImageField(upload_to='img/consultant')
#     score = models.IntegerField(default=0)
#     telegram = models.CharField(max_length=50, null=True, blank=True)
#     instagram = models.CharField(max_length=50, null=True, blank=True)
#     whatsapp = models.CharField(max_length=50, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     tel = models.CharField(max_length=11, null=True, blank=True)
#     sex = models.BooleanField(null=True, blank=True)
#
#
# class Student(CustomUser):
#     age = models.IntegerField(null=True, blank=True)
#     reshte = models.CharField(max_length=50, null=True, blank=True)
#     Consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, null=True, blank=True)


# class Profile(models.Model):
#     User = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     records = models.CharField(max_length=50, null=True, blank=True)
#     image = models.ImageField(upload_to='img/consultant', null=True, blank=True)
#     score = models.IntegerField(default=0, null=True, blank=True)
#     telegram = models.CharField(max_length=50, null=True, blank=True)
#     instagram = models.CharField(max_length=50, null=True, blank=True)
#     whatsapp = models.CharField(max_length=50, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     tel = models.CharField(max_length=11, null=True, blank=True)
#     sex = models.BooleanField(null=True, blank=True)
#     consultant = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
