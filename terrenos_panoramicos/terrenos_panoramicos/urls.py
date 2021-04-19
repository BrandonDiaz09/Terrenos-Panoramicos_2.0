"""terrenos_panoramicos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from os import name
from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from users import views as users_views
from ventas import views as catalogo_views
from empresa import views as terrenospa_views

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    #Empresa
    path('', terrenospa_views.home, name='home'),
    path('ofrece/', terrenospa_views.ofrecer_predio, name ='ofrece'),
    path('conocenos/', terrenospa_views.conocenos, name ='conocenos'),
    
    #Ventas
    path('ventas/catalogo/', catalogo_views.InmuebleView.as_view(), name ='catalogo' ),

    #Users 
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
    path('<str:username>/', view=users_views.UserDetailView.as_view(), name='detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
