from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import ProductForm, RegistrationForm, ManufacturerForm
from .models import Product, Category, Manufacturer

def aboutCourseProject(request):
    return render(request, 'electronicsApp/AboutCourseProject.html')


def aboutTeamMembers(request):
    member_name_1 = 'Dimash Nogaibaev'
    born_year_1 = 2001
    description_1 = 'Very responsible, disciplined, attentive, friendly, helpful, cheerful and stubborn.'
    image_path_1 = 'images/dimash.jpg'
    data_1 = {'member_name': member_name_1, 'born_year': born_year_1, 'description': description_1,
              'image_path': image_path_1}

    member_name_2 = 'Temirlan Zhumanbayev'
    born_year_2 = 2001
    description_2 = 'Calm, pedantic, purposeful, attentive,responsible, persistent and ambitious.'
    image_path_2 = 'images/temirlan.jpg'
    data_2 = {'member_name': member_name_2, 'born_year': born_year_2, 'description': description_2,
              'image_path': image_path_2}

    dataToHtml = {'first': data_1, 'second': data_2}
    return render(request, 'electronicsApp/AboutTeamMembers.html', context=dataToHtml)


def aboutDevelopersContacts(request):
    team_leader = {'name': 'Nogaibaev Dimash', 'phone_number': '+7 747 333 42 15', 'email': 'nogaybaevd11@list.ru',
                   'office_hours': ['Mon, 11.00 - 13.00', 'Tue, 8.00 - 10.50']}
    developer = {'name': 'Zhumanbayev Temirlan', 'phone_number': '+7 707 653 95 31', 'email': 'zhumanbaev02@mail.ru',
                 'office_hours': ['Mon, 11.00 - 13.00', 'Tue, 8.00 - 10.50']}
    dataToHtml = {'head_office_address': '34/1 Manas Street, Almaty 050000',
                    'team_leader': team_leader,
                    'developer': developer}
    return render(request, 'electronicsApp/AboutDevelopersContacts.html', context=dataToHtml)


def home(request):
    television = Product.objects.get(id=19)
    televisions = Product.objects.filter(category=3)
    return render(request, 'electronicsApp/Home.html', {'television': television, 'televisions': televisions})


def smartphones(request):
    smartphones = Product.objects.filter(category=1)
    dataToHtml = {'header': 'Smartphones', 'smartphones': smartphones}
    return render(request, 'electronicsApp/Smartphones.html', context=dataToHtml)


def notebooks(request):
    notebooks = Product.objects.filter(category=2)
    dataToHtml = {'header': 'Notebooks', 'notebooks': notebooks}
    return render(request, 'electronicsApp/Notebooks.html', context=dataToHtml)


def televisions(request):
    televisions = Product.objects.filter(category=3)
    dataToHtml = {'header': 'Televisions', 'televisions': televisions}
    return render(request, 'electronicsApp/Televisions.html', context=dataToHtml)


def tablets(request):
    tablets = Product.objects.filter(category=4)
    dataToHtml = {'header': 'Tablets', 'tablets': tablets}
    return render(request, 'electronicsApp/Tablets.html', context=dataToHtml)


def homeAppliances(request):
    homes = Product.objects.filter(category=5)
    dataToHtml = {'header': 'Home Appliances', 'homes': homes}
    return render(request, 'electronicsApp/HomeAppliances.html', context=dataToHtml)


def contactUs(request):
    return render(request, 'electronicsApp/ContactUs.html')


def login(request):
    return render(request, 'electronicsApp/accounts/Login.html')


def registration(request):
    return render(request, 'electronicsApp/Registration.html')


def changePassword(request):
    return render(request, 'electronicsApp/accounts/ResetPassword.html')


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    manufacturers = Manufacturer.objects.all()
    dataToHtml = {'products': products, 'categories': categories, 'manufacturers': manufacturers}
    return render(request, 'electronicsApp/Products.html', context=dataToHtml)


def createProduct(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('productsPage')
    return render(request, 'electronicsApp/CreateProduct.html', {'form': form})


def createManufacturer(request):
    form = ManufacturerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('productsPage')
    return render(request, 'electronicsApp/CreateManufacturer.html', {'form': form})


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'electronicsApp/ProductDetails.html', {'product': product})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    #fields = ['product_name', 'product_price', 'category', 'manufacturer', 'product_description']
    success_url = '/all-products'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/all-products'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'electronicsApp/accounts/Profile.html'


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('loginPage')
    template_name = 'electronicsApp/accounts/Registration.html'

