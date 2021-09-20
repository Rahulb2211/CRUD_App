from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    marks = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.id}  = = =  {self.name}  = = =   {self.email}  = = =   {self.password}  === {self.marks}"