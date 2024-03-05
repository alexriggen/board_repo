from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 30,null = True, unique = True)
    email = models.EmailField(unique = True)
    bio = models.TextField(null = True)
    avatar = models.ImageField(null = True, default="avatar.svg")
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

class Genre(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
class Game(models.Model):

    name = models.CharField(max_length = 40, null = True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    capacity = models.IntegerField(default = 5)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name
    
class Meeting(models.Model):

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) 
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True) #creates a many to many field, related name is used because we already used User
    date = models.DateField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created'] # - makes it go in descending order

    def __str__(self):
        return str(self.name)
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-updated', '-created'] # - makes it go in descending order

    def __str__(self):
        return self.body[0:50] #outputs first 50 characters of body if only message is called