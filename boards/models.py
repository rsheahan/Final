from django.db import models

# Create your models here.


class User(models.Model):
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
    pic_name = models.CharField(max_length=60)
    pic_description = models.CharField(max_length=200)
    pic_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.pic_name
