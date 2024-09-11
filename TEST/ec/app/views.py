from django.shortcuts import HttpResponse, render
from django.views import View
from.models import Product
from django.db.models import Count
from .forms import CustomerRegistrationForm
from django.contrib import messages

def home(request):
    return render(request, 'app/home.html')
    

def about(request):
    return render(request, 'app/about.html')


def contact(request):
    return render(request, 'app/contact.html')\



class CategoryView(View):
    def get(self, request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html',locals())

class CategoryTitle(View):
    def get(self, request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html',locals())

class ProductDetails(View):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/product_details.html',locals())


class CustomerRegistrationView(View):

    def get(self, request):
        form= CustomerRegistrationForm()
        return render(request, 'app/customer_registration.html',locals())

    def post(self, request):
        form= CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Registration successful.')

        else:
            messages.warning(request, 'Invalid form submission.')


        return render(request, 'app/customer_registration.html',locals())