"""onlineB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views
from projects.forms import signup_form
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/register/',RegistrationView.as_view(form_class=signup_form,template_name="django_registration/registration_form.html"),{"next_page": '/'}),
    path('accounts/login/', views.LoginView.as_view(template_name="django_registration/login.html")),
    path('accounts/logout/' ,views.LogoutView.as_view(template_name="django_registration/logout.html"),name='logout'),
   # path('', TemplateView.as_view(template_name='home.html'), name='home')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
