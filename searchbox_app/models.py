from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobileno=models.CharField(max_length=14)
    image=models.ImageField(upload_to='upload/')
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()

    def __str__(self):
        return self.name + self.username

    