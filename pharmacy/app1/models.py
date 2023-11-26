from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Medicine(models.Model):
    medicinename=models.CharField(max_length=50)
    medicinetype=models.CharField(max_length=50)
    medicinestock=models.CharField(max_length=50)
    medicineprice=models.CharField(max_length=50)


    def __str__(self):
        return self.medicinename


class Sales(models.Model):
    customername=models.CharField(max_length=50)
    customercontact=models.CharField(max_length=50)
    medicine=models.CharField(max_length=50)

    def __str__(self):
        return self.customername



