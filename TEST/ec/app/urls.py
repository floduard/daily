from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, PasswordChangeForm


urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>",views.ProductDetails.as_view(),name="product-detail"), 
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.address, name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(), name='updateAddress'),


#login authentication
    path("registration/",views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path("accounts/login/",auth_views.LoginView.as_view(template_name="app/login.html", authentication_form = LoginForm), name="login"),
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="app/password_reset.html", email_template_name="app/password_reset.html", form_class=PasswordChangeForm),name="password_reset")

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

