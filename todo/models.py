from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Task(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=200, null=True)
    todo_date = models.DateField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
