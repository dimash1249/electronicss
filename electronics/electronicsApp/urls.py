from django.urls import path
from django.contrib.auth import views as auth_views
from electronicsApp.views import aboutTeamMembers, aboutDevelopersContacts, aboutCourseProject
from electronicsApp.views import home, smartphones, notebooks, televisions, homeAppliances, tablets, contactUs, product
from electronicsApp.views import login, registration, changePassword
from electronicsApp.views import createProduct, createManufacturer, products, ProductUpdateView, ProductDeleteView, RegistrationView
from electronicsApp.forms import LoginForm


urlpatterns = [
    # user urls
    path('', home, name='homePage'),
    path('about-course-project/', aboutCourseProject, name='aboutCourseProjectPage'),
    path('about-team-members/', aboutTeamMembers, name='aboutTeamMembersPage'),
    path('about-developers-contacts/', aboutDevelopersContacts, name='aboutDevelopersContactsPage'),
    path('product-information/', product, name='productInformationPage'),
    path('smartphones/', smartphones, name='smartphonesPage'),
    path('notebooks/', notebooks, name='notebooksPage'),
    path('televisions/', televisions, name='televisionsPage'),
    path('tablets/', tablets, name='tabletsPage'),
    path('home-appliances/', homeAppliances, name='homeAppliancesPage'),
    path('product/<id>', product, name='productDetailsPage'),
    path('contact-us/', contactUs, name='contactUsPage'),
    path('login/', login, name='loginPage'),
    path('registration/', registration, name='registrationPage'),

    # admin urls
    path('all-products/', products, name='productsPage'),
    path('create-a-new-product/', createProduct, name='createProductPage'),
    path('create-a-new-manufacturer/', createManufacturer, name='createManufacturerPage'),
    path('update-product/<pk>', ProductUpdateView.as_view(template_name='electronicsApp/UpdateProduct.html'), name='updateProductPage'),
    path('delete-product/<pk>', ProductDeleteView.as_view(template_name='electronicsApp/DeleteProduct.html'), name='deleteProductPage'),

    # login system
    path('accounts/login', auth_views.LoginView.as_view(template_name='electronicsApp/accounts/Login.html', authentication_form=LoginForm), name='loginPage'),
    path('accounts/logout', auth_views.LogoutView.as_view(template_name='electronicsApp/accounts/'), name='logoutPage'),
    path('account/profile', auth_views.TemplateView.as_view(template_name='electronicsApp/accounts/Profile.html'), name='profilePage'),
    path('account/register/', RegistrationView.as_view(), name='registrationPage'),
    path('account/password-change/', changePassword, name='changePasswordPage'),
]
