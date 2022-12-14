from django.db import models

# Create your models here.
class Seller_table(models.Model):
    seller_name=models.CharField(max_length=100)
    seller_phone=models.CharField(max_length=100)
    seller_raw=models.CharField(max_length=50)
    seller_price=models.CharField(max_length=10)
    desc=models.CharField(max_length=500,default="")
    img=models.ImageField( upload_to='images/',default="")

    def __str__(self):
        return self.seller_raw
    
# testing