from django.db import models

# Create your models here.

class Product(models.Model):
    userid = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'product'  # specifying the correct table name here

class APIModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TaxField()
    
    def __str__(self):
        return self.title