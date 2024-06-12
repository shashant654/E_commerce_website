from django.contrib import admin
from django.urls import path
from .import views

from myapp.controller import authview, cart, wishlist,checkout,order

urlpatterns = [
          path('',views.home,name="home"),
          path("collections/", views.collections, name="collections"),
          path('collections/<str:slug>',views.collectionsview, name ="collectionsview"),
          path('collections/<str:cate_slug>/<str:prod_slug>',views.productview, name ="productview"),

          path("register/", authview.register , name="register"),
          path("login/", authview.loginpage , name="loginpage"),
          path("logout/", authview.logoutpage , name="logout"), 
          path('add-to-cart',cart.addtocart,name="addtocart"),
          path('cart/',cart.viewcart,name="cart"),
          path('update-cart',cart.updatecart,name='updatecart'),
          path('delete-cart-item',cart.deletecartitem,name='deletecartitem'),
          path('wishlist/',wishlist.index,name="wishlist"),
          path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
          path('delete-wishlist-item',wishlist.deletewishlistitem,name = 'deletewishlistitem'),
          path('checkout',checkout.index,name="checkout"),
          path('place-order',checkout.placeorder,name="placeorder"),

          path('proceed-to-pay',checkout.razorpaycheck),
          path('my-orders',order.index,name="myorders"),
          path('view-order/<str:t_no>',order.vieworder,name="orderview")


]




# def productview(request,cate_slug,prod_slug):
#           if(Category.objects.filter(slug = cate_slug,status = 0)).exists():
#                     if(Product.objects.filter(slug=prod_slug,status=0)).exists():
#                               product = Product.objects.filter(slug= prod_slug,status=0).first()
#                               context = {'product':product}

#                     else:
#                               messages.error(request,"No such product found")
#                               return redirect('collections')
#           else:
#                     messages.error(request,"No such category found")
#                     return redirect('collections')
#           return render(request,'store/products/view.html',context)

# import logging
# logger = logging.getLogger(__name__)

# def productview(request, cate_slug, prod_slug):
#     try:
#         logger.debug(f"Category Slug: {cate_slug}, Product Slug: {prod_slug}")
#         category = Category.objects.get(slug=cate_slug, status=0)
#         product = Product.objects.filter(category=category, slug=prod_slug, status=0).first()
#         if not product:
#             messages.error(request, "No such product found")
#             return redirect('collections')
#         context = {'product': product}
#         return render(request, 'store/products/view.html', context)
#     except Category.DoesNotExist:
#         messages.error(request, "No such category found")
#         return redirect('collections')


# def productview(request, cate_slug, prod_slug):
#     try:
#         logger.debug(f"Category Slug: {cate_slug}, Product Slug: {prod_slug}")
#         category = Category.objects.get(slug=cate_slug, status=0)
#         product = Product.objects.get(category=category, slug=prod_slug, status=0)
#         context = {'product': product}
#         return render(request, 'store/products/view.html', context)
#     except Category.DoesNotExist:
#         messages.error(request, "No such category found")
#         return redirect('collections')
#     except Product.DoesNotExist:
#         messages.error(request, "No such product found")
#         return redirect('collections')
