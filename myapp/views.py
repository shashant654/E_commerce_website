from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.


def home(request):
          return render(request,'store/index.html')

def collections(request):
          category = Category.objects.filter(status = 0)
          context = {'category': category}
          return render(request,'store/collections.html',context)


def collectionsview(request, slug):
          if(Category.objects.filter(slug=slug,status=0)):
                    products = Product.objects.filter(category__slug = slug)
                    category = Category.objects.filter(slug=slug).first()
                    context = {'products': products, 'category':category}
                    return render(request,'store/products/index.html',context)
          else:
                    messages.warning(request,"No such category found")
                    return redirect('collections')



def productview(request,cate_slug,prod_slug):
          if(Category.objects.filter(slug = cate_slug,status = 0)).exists():
                    if(Product.objects.filter(slug=prod_slug,status=0)).exists():
                              product = Product.objects.filter(slug= prod_slug,status=0).first()
                              context = {'product':product}

                    else:
                              messages.error(request,"No such product found")
                              return redirect('collections')
          else:
                    messages.error(request,"No such category found")
                    return redirect('collections')
          return render(request,'store/products/view.html',context)

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

