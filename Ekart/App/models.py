from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class User(AbstractUser):
	t=[(1,'customer'),(2,'seller'),(3,'guest')]
	role=models.CharField(max_length=10,choices=t)


class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
	name=models.CharField(max_length=200,null=True)
	email=models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	pid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	category=models.CharField(max_length=200,null=True)
	itemname=models.CharField(max_length=200,null=True)
	price= models.FloatField()
	image=models.ImageField(null=True,blank=True)

	def __str__(self):
		return self.itemname

class Order(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
	date_order=models.DateTimeField(auto_now_add=True)
	complete=models.BooleanField(default=False,null=True,blank=False)
	transaction_id=models.CharField(max_length=200,null=True)

	def __str__(self):
		return str(self.id)


class OrderItem(models.Model):
	product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
	order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
	qunatity=models.IntegerField(default=0,null=True,blank=True)
	date_added=models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
	order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
	address=models.CharField(max_length=200,null=True)
	city=models.CharField(max_length=200,null=True)
	state=models.CharField(max_length=200,null=True)
	zipcode=models.CharField(max_length=200,null=True)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
 		
class credit(models.Model):
	creditno=models.IntegerField(null=False)
	cvv=models.IntegerField(null=False)
	monyer=models.DateTimeField(null=False)

class Seller(models.Model):
	name=models.CharField(max_length=40,null=True)
	phoneno=models.IntegerField()
	email=models.CharField(max_length=100,null=True)
	address=models.CharField(max_length=200,null=True)
	image=models.ImageField(null=False)


class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

class Category(models.Model):
	cname=models.CharField(max_length=20)
	def __str__(self):
		return self.cname

class RoleRest(models.Model):
	t=[(1,'seller'),(2,'customer')]
	uname= models.CharField(max_length=30)
	roletype = models.PositiveIntegerField(choices=t)
	prf = models.CharField(max_length=250)
	is_checked=models.BooleanField(default=0)
	uid= models.OneToOneField(User,on_delete=models.CASCADE)