from django.db import models
from datetime import datetime,date

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    address=models.CharField(max_length=250,null=True)
    gst=models.CharField(max_length=50,null=True)
    date_created=models.DateTimeField()

    def __str__(self):
        return self.name
class Tags(models.Model):
    name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY=(
    ('Projects','projects'),('AMC','AMC'),('Sales','Sales'),('Supplier','Supplier'),
     )
    name=models.CharField(max_length=50,null=True)
    price=models.FloatField()
    category=models.CharField(max_length=50,null=True,choices=CATEGORY)
    number=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200, null=True,blank=True)
    date_created=models.DateTimeField(null=True)
    tags=models.ManyToManyField(Tags)
        
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS =(
        ('pending','pending'),
        # ('Out for Delivery','Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer=models.CharField(max_length=50,null=True)
    product=models.CharField(max_length=50,null=True)
    date_created=models.DateTimeField(null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    def __str__(self):
        return self.product

class Project(models.Model):
    STATUS=(
        ("New","New"),("In Progress", "In Progress"),('Completed','Completed'),

    )
    name=models.CharField(max_length=50,null=True)
    customer=models.ForeignKey(Customer, null=True,on_delete=models.SET_NULL)
    startdate=models.DateField(null=True)
    def __str__(self):
        return self.name



class Supplier(models.Model):
    companyName = models.CharField(max_length=100, blank=False)
    contactPerson =  models.CharField(max_length=30, default="None")
    emailId = models.EmailField(default="")
    address=models.CharField(max_length=150,null=True)
    phoneNo = models.IntegerField(null=True)
    gst_id=models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.companyName




class Room(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Message(models.Model):
    value=models.CharField(max_length=1000000)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=10000)
    room=models.CharField(max_length=1000)
    def __str__(self):
        return self.user

    



