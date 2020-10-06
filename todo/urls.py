"""todo URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from daytasks.views import home, signup, delete, add_task, edit_task


urlpatterns = [
     path('todo/', home, name='home'),
     path('todo/home/', home, name='home'),
     path('todo/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
     path('todo/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('signup/', signup, name='signup'),
     path('todo/delete/<int:task_id>', delete, name='delete'),
     path('todo/add/', add_task, name='add'),
     path('todo/edit/<int:task_id>', edit_task, name='edit'),
     path('todo/admin/', admin.site.urls),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
