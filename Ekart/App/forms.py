from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from App.models import Customer,Product,User,Seller,Order,RoleRest,Category





class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
	class Meta:
		model=User
		fields=['username','email']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"username",
			}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"userEmail"})


		}

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=['category','itemname','price','image']
		widgets={
		"category":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"category",
			}),
		"itemname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"itemname",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"price",
			}),
		}


class Sellerform(forms.ModelForm):
	class Meta:
		model=Seller
		fields=['name','phoneno','email','address','image']
		widgets={
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"name"
			}),
		"phoneno":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"phoneno"
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"email"
			}),
		"address":forms.TextInput(attrs={"class":"form-control","placeholder":"address","required":True})
		}

class CartForm(forms.ModelForm):
	class Meta:
		model=Product
		fields=['itemname','price','image']
		widgets={
		"itemname":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"itemname",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"itemname",
			}),
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=["cname"]
		widgets={
		"cname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter cname"}),
		}

class RoleR(forms.ModelForm):
	class Meta:
		model = RoleRest
		fields= ["roletype","prf"]
		widgets={
		"uname":forms.TextInput(attrs={"class":"form-control","readonly":True}),

		"roletype":forms.Select(attrs = {"class": "form-control",}),
		"prf":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter proof"}),


		}


 		