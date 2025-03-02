from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Company(models.Model):

    choices = [
        ("IT", "IT"),
        ("Non - IT", "Non - IT"),  
        ("Networking", "Networking")
    ]
    Company_id = models.AutoField(primary_key=True)
    Company_name = models.CharField(max_length=100)
    Company_address = models.TextField()
    Company_rating = models.IntegerField()
    Company_type = models.CharField(max_length=100, choices=choices)
    Company_about = models.TextField()

    def __str__(self):
        return self.Company_name

    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.AutoField(primary_key=True)
    address = models.TextField()
    join_date = models.DateField(models.DateField(_("Join Date"),auto_now_add=True))
    company = models.ForeignKey(Company, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
