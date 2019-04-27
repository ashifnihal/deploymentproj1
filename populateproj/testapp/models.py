from django.db import models
class CarDataModel(models.Model):
    sno=models.IntegerField()
    brand=models.CharField(max_length=256)
    model=models.CharField(max_length=256)
    fuel=models.CharField(max_length=256)
    year=models.IntegerField()
    cc=models.FloatField()
    mobileno=models.IntegerField()


# Create your models here.
