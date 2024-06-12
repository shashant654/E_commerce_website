from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponse

from django.http.response import JsonResponse

from myapp.models import Product, Cart, Order, OrderItem

def index(request):
          orders = Order.objects.filter(user=request.user)
          context = {'orders': orders}
          print(context)
          return render(request,"store/orders/index.html", context)

def vieworder(request,t_no):
          order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
          orderitems = OrderItem.objects.filter(order=order)
          context = {'order':order, 'orderitems':orderitems}
          return render(request,"store/orders/view.html",context)
