from django.urls import path
from App import views
from django.contrib.auth import views as v

urlpatterns =[
    path('store/',views.store,name="store"),
    path('',views.home,name="home"),
    path('cart/',views.cart,name="carts"),
    path('checkout/',views.checkout,name="checkout"),
    path('Payment/',views.payment,name="pay"),
    path('product/',views.product,name="product"),
    path('lg/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
    path('lgo/',v.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('reg/',views.registration,name="reg"),
    path('join/',views.joinus,name="join"),
    path('del/<int:id>/',views.deletedata,name="delete"),
    path('seller/',views.sellerdetails,name="seller"),
    path('cardde/',views.carddetails,name="cardde"),
    path('addcart/<int:id>/',views.addcart,name="addcart"),
    path('remove/<int:id>/',views.remove,name="remove"),
    path('rlrq',views.rolreq,name='rr'),
    path('category/',views.addcategory,name="addcategory"),


]