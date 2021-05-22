from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from App.models import Product,Cart,Seller,Category
from App.forms import UsForm,ProductForm,Sellerform,CartForm,RoleR,CategoryForm
from django.core.mail import send_mail
from Ekart import settings
from django.core.mail import EmailMessage
from django.contrib import messages

# Create your views here.
def home(req):
	data=Product.objects.all()
	return render(req,'html/home.html',{'info':data})


def store(req):
	data=Product.objects.all()
	return render(req,'html/store.html',{'info':data})

def cart(request):
	a=Cart.objects.filter(user_id=request.user.id)
	sum=0
	count=0
	for i in a:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/cart.html',{'info':a})

def checkout(req):
	return render(req,'html/checkout.html')

def payment(req):
	if req.method=="POST":
		cnum=req.POST['cnum']
		cvv=req.POST['cvvnum']
		my=req.POST['date']
		data=credit.objects.create(creditno=cnum,cvv=cvv,monyer=my)
	return render(req,'html/payment.html')


def registration(req):
	if req.method=="POST":
		p=UsForm(req.POST)
		if p.is_valid():
			e = p.save(commit=False)
			sb = "Testing Email For FarMeKart"
			mg = "Hi Welcome {}. You have successfully registered for FarMeKart portal.".format(e.username)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[e.email])
			if snt == 1:
				e.save()
				return redirect('/lg')
			else:
				return redirect('/')
	p=UsForm()
	return render(req,'html/registration.html',{'u':p})

def product(request):
	if request.method=="POST":
		j=ProductForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.uid_id=request.user.id
			i.save()
	j=ProductForm()
	k=Product.objects.all()
	return render(request,'html/product.html',{'u':j,'info':k})

def joinus(req):
	if req.method=="POST":
		a=Sellerform(req.POST,req.FILES)
		if a.is_valid():
			a.save()
			return redirect('/store')
	a=Sellerform()
	return render(req,'html/joinus.html',{'s':a})

def deletedata(req,id):
	data=Product.objects.get(id=id)
	data.delete()
	return redirect('/product')

def sellerdetails(req):
	return render(req,'html/sellerdetails.html')

def carddetails(req):
	return render(req,'html/cartdetails.html')

def addcart(request,id):
	a=Product.objects.get(id=id)
	if request.method=="POST":
		c=Cart(user_id=request.user.id,product_id=a.id)
		c.save()
		return redirect('/store')
	return render(request,'html/addcart.html')

def remove(req,id):
	data=Cart.objects.get(id=id)
	data.delete()
	return redirect('/cart')

def yourproducts(request):
	d=Product.objects.filter(pid_id=request.user.id)
	return render(request,'html/yourproducts.html',{'data':d})

def rolreq(request):
	if request.method== "POST":
		k =RoleR(request.POST)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			s.save()
	k=RoleR()
	return render(request,'html/rolreq.html',{'a':k})

def addcategory(request):
	if request.method=="POST":
		a=CategoryForm(request.POST)
		if a.is_valid():
			a.save()
	cf=CategoryForm()
	return render(request,'html/addcategory.html',{'c':cf})
