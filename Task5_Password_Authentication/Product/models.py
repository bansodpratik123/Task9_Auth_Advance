from django.db import models

# Create your models here.

class Laptops(models.Model):
    Model_Name=models.CharField(max_length=32)
    Company=models.CharField(max_length=32)
    RAM=models.IntegerField()
    ROM=models.IntegerField()
    Processor=models.CharField(max_length=32)
    Weight=models.FloatField()
    Price=models.FloatField()


class Documents(models.Model):
    ModelName=models.OneToOneField(Laptops,on_delete=models.CASCADE)
    Document=models.FileField(upload_to='images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

class Documents1(models.Model):
    ModelName=models.OneToOneField(Laptops,on_delete=models.CASCADE)
    Document=models.FileField(upload_to='images/')
