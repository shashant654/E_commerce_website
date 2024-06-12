from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponse

from django.http.response import JsonResponse

from myapp.models import Product, Cart, Order, OrderItem

@login_required(login_url='loginpage')
def index(request):
          rawcart = Cart.objects.filter(user = request.user)
          for item in rawcart:
                    if item.product_qty > item.product.quantity:
                              Cart.objects.delete(id=item.id)
                              print(item.id)
          
          cartitems = Cart.objects.filter(user=request.user)
          total_price = 0
          for item in cartitems:
                    total_price = total_price + item.product.selling_price * item.product_qty

          context = {'cartitems' : cartitems, 'total_price': total_price}
          return render(request, 'store/checkout.html',context)



@login_required(login_url='loginpage')
def placeorder(request):
       if request.method == 'POST':
             neworder = Order()
       #       changing
             neworder.user = request.user
             neworder.fname = request.POST.get('fname')
             neworder.lname = request.POST.get('lname')
             neworder.email = request.POST.get('email')
             neworder.phone = request.POST.get('phone')
             neworder.address = request.POST.get('address')
             neworder.city = request.POST.get('city')
             neworder.state = request.POST.get('state')
             neworder.country = request.POST.get('country')
             neworder.pincode = request.POST.get('pincode')

             neworder.payment_mode = request.POST.get('payment_mode')
             neworder.payment_id = request.POST.get('payment_id')


             cart = Cart.objects.filter(user=request.user)
             cart_total_price = 0
             for item in cart:
                    cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
          
             neworder.total_price = cart_total_price
             trackno = 'shashant' + str(random.randint(1111111,9999999))

             # chanign
             while Order.objects.filter(tracking_no = trackno).exists():
                    trackno = "shashant" + str(random.randint(1111111,9999999))

             neworder.tracking_no = trackno
             neworder.save()

             neworderitems = Cart.objects.filter(user=request.user)
       #       changing
       #       for item in neworderitems:
             for item in cart:
                    OrderItem.objects.create(
                              order = neworder,
                              product = item.product,
                              price = item.product.selling_price,
                              quantity = item.product_qty
                    )

                    # to decrease the product quantity from availabel stock
              #       changin
                    orderproduct = Product.objects.get(id = item.product_id)

              #       orderproduct = Product.objects.filter(id = item.product_id).first()
                    orderproduct.quantity = orderproduct.quantity - item.product_qty
                    orderproduct.save()

             # to clear user's cart 
       #       changing
       #       Cart.objects.filter(user=request.user).delete()
             cart.delete()


             payMode = request.POST.get('payment_mode')
             if (payMode == "Paid by Razorpay"):
                return JsonResponse({'status':"Your order has been placed successfully"})
             else:
                messages.success(request, "Your order has been placed successfully")
                return redirect('/')


       return redirect('/')


@login_required(login_url='loginpage')
def razorpaycheck(request):
             cart = Cart.objects.filter(user=request.user)
             total_price = 0
             for item in cart:
                    total_price = total_price + item.product.selling_price * item.product_qty
             
             return JsonResponse({
              'total_price':total_price
             })


# def orders(request):
#        return HttpResponse("My orders page")