from django.shortcuts import HttpResponse, render,redirect
from django.views import View
from.models import Product, Customer
from django.db.models import Count
from .forms import CustomerRegistrationForm, CustomerProfileForm
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


class ProfileView(View): 
    def get(self, request):
        form= CustomerProfileForm()
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form= CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            mobile=form.cleaned_data['mobile']
            locality=form.cleaned_data['locality']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, mobile=mobile, locality=locality,state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'conglulations! Profile saved successfully.')
        else:
            messages.warning(request, 'Invalid Input data')
        return render(request, 'app/profile.html', locals())


def address(request):
    add = Customer.objects.filter(user=request.user)
    return redirect('address')



class updateAddress(View):
    def get(self, request,pk):
        add = Customer.objects.get(pk=pk)
        form= CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html',locals())

    def post(self, request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.mobile=form.cleaned_data['mobile']
            add.locality=form.cleaned_data['locality']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'conglulations! Profile saved successfully.')
        else:
            messages.warning(request, 'Invalid Input data')
        return redirect('address')

        
