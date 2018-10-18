"""entry_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from inventoryentry import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

urlpatterns = [
    url(r'^django_popup_view_field/', include('django_popup_view_field.urls', namespace="django_popup_view_field")
    ),
    url('admin/', admin.site.urls, name='admin'),
    url('inventory/', include('django.contrib.auth.urls')),
    url(r'^login/$',auth_views.LoginView.as_view(), name="login"),
    url(r'^logout/$',auth_views.LogoutView.as_view(), name="logout"),
    url(r'^logout/$',auth_views.LogoutView.as_view(), {'next_page': '/login/'}, name='logout'),    
    
    
    url(r'^entries/$', views.entries_list, name='entries_list'),
    url(r'^entries/create$', views.entries_create, name='entries_create'),
    url(r'^entries/(?P<id>\d+)/update$', views.entries_update, name='entries_update'),
    url(r'^entries/(?P<id>\d+)/delete$', views.entries_delete, name='entries_delete'),
    
    url(r'^entries/csv/$', views.export_csv, name='export_csv'),
    url(r'^entries/excel/$', views.export_excel, name='export_excel'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
