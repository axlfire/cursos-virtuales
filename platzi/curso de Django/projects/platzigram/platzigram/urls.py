
"""platzigram URL Configuration

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
# TODO: revisar documentacion urls
# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#local
from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views
urlpatterns = [
#se accede creando un super usuario con manage.py
    path('admin/', admin.site.urls),

    path('HelloWorld/',local_views.HelloWorld,name='hello_world'),
    path('hi/',local_views.hi,name='hi'),
    path('sorted/',local_views.calc,name='sort'),
    path('menor/<str:name>/<int:age>',local_views.menor,name='hi'),
    #posts path:
    path('posts/', posts_views.list_posts, name='feed'),
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# la siguiente linea le suma a urlpatterns una url estatica con el valor MEDIA_URL
# y MEDIA_ROOT, el primero es donde se encuentra la media que estamos buscando
# y el segundo en donde nos encontramos
# MEDIA_URL y MEDIA_ROOT se confiuran en settings:
#
# QUESTION: se supone que con esto ya deberia poder ver imagenes si la abro desde admin, no lo muestra
# nota1:no esta creando la carpeta media, por ende no encuentra la imagen
# nota2:corregido lo de arriba,ya crea la carpeta, pero igual no encuentra la imagen
