from django.db import models

# Create your models here.
class addition(models.Model):
    temperature=models.IntegerField()
    humidity=models.IntegerField()
    pressure=models.IntegerField()
    timestamp=models.TextField()
