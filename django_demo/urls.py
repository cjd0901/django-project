"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app01.views import classes
from app01.views import students
from app01.views import ajax

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classes',classes.get_classes),
    path('add_classes',classes.add_classes),
    path('del_classes',classes.del_classes),
    path('edit_classes',classes.edit_classes),
    path('set_teachers',classes.set_teachers),

    path('students',students.get_students),
    path('add_students',students.add_students),
    path('del_students',students.del_students),
    path('edit_students',students.edit_students),

    path('ajax1',ajax.ajax1),
    path('ajax2',ajax.ajax2),
    path('ajax3',ajax.ajax3),
    path('ajax4',ajax.ajax4),
    path('ajax5',ajax.ajax5),
    path('ajax6',ajax.ajax6),
]
