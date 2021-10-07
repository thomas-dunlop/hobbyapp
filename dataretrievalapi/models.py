from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    notes = models.CharField(max_length=1000)
    status = models.CharField(max_length=200)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Recipe(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    projects = models.ManyToManyField(Project)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Step(models.Model):
    description = models.CharField(max_length = 200)
    orderValue = models.IntegerField(default = 1)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField(max_length = 200)
    partNumber = models.CharField(max_length = 200)
    company = models.CharField(max_length = 200)
    link = models.URLField()
    category = models.CharField(max_length = 200)
    steps = models.ManyToManyField(Step)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Inventory(models.Model):
    lotNumber = models.CharField(max_length = 200)
    expiryDate = models.DateField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
