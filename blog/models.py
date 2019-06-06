from django.db import models
from datetime import date
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=190)
    subject = models.CharField(max_length=120)
    date = models.DateField(default=date.today)
    discreption = models.TextField(null=True, blank=True)
