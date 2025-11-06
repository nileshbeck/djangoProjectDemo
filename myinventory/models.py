from django.db import models
 
# Create your models here.

# class AuthUser(AbstractUser):
#     phone=models.TextField

#define the structure of database tables
class customer(models.Model):
    """ tampspmp=models.DateTimeField(auto_now_add= True) adding time of submit form
    """
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    address=models.TextField()
    def __str__(self):
        return self.name
    #this functions controls how the object will be shown in admin panel
class Categories(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

# class product(models.Model):
class vender(models.Model):
    vender_name=models.CharField(max_length=20)
    contact_person=models.CharField(max_length=20)
    Phone=models.CharField(max_length=12)
    Email=models.EmailField()
    Address=models.TextField()
    def __str__(self):
        return self.name

class product(models.Model):
    Product_name=models.CharField(max_length=20)
    Category=models.CharField(max_length=20)
    Vender=models.CharField(max_length=12)
    Quantity=models.IntegerField()
    Purchase_price=models.IntegerField()
    Selling_price=models.IntegerField()
    
    def __str__(self):
        return self.name
        
