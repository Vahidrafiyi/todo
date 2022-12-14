from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=True, blank=True)
    photo = models.ImageField(upload_to='/profiles/', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} profile'

class Task(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title    = models.CharField(max_length=128)
    note     = models.TextField(null=True, blank=True)
    file     = models.FileField(upload_to='/tasks/', null=True, blank=True)
    created  = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.user.username} {self.title}'
    
