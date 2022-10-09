from django.db import models

# Create your models here.
class Buyer_table(models.Model):
    buyer_name=models.CharField(max_length=50)
    buyer_phone=models.CharField(max_length=50)
    buyer_adhaar=models.CharField(max_length=50)
    buyer_pass1=models.CharField(max_length=50)



    
