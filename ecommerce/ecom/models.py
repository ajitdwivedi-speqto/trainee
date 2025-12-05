from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    specifications = models.TextField()
    img=models.ImageField(upload_to='product_images/',null=True,blank=True)