"""final URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path


from boards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^userIndex/', views.userIndex, name='userIndex'),
    url(r'^register/', views.register, name='register'),
    url(r'^addUser', views.addUser, name='addUser'),
    url(r'^loginView/', views.loginView, name='loginView'),
    url(r'^checkUser', views.checkUser, name='checkUser'),
    url(r'^logoutView', views.logoutView, name='logoutView'),
    url(r'^profileView', views.profileView, name='profileView'),
    url(r'^viewBoard', views.viewBoard, name='viewBoard'),
    url(r'^viewPicture', views.viewPicture, name='viewPicture'),
    url(r'^addPicture', views.addPicture, name='addPicture'),
    url(r'^editPicture', views.editPicture, name='editPicture'),
    url(r'^submitPicture', views.submitPicture, name='submitPicture'),
    url(r'^deletePicture', views.deletePicture, name='deletePicture')


]
