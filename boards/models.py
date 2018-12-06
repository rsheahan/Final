from __future__ import unicode_literals

from django.db import models

# Create your models here.


class localUsers(models.Model):
    username = models.CharField(max_length=60)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username


class Board(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Picture(models.Model):
    pic = models.ImageField(default="default.jpg")
    picName = models.CharField(max_length=60)
    picDescription = models.CharField(max_length=200)
    picDate = models.DateTimeField()
    owner = models.ForeignKey(localUsers, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.picName
