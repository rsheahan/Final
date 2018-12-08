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
from django.urls import path, include

from django.conf.urls.static import static


from boards import views
from final import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^userIndex/', views.userIndex, name='userIndex'),
    url(r'^register/', views.register, name='register'),
    url(r'^loginView/', views.loginView, name='loginView'),
    url(r'^checkUser', views.checkUser, name='checkUser'),
    url(r'^logoutView', views.logoutView, name='logoutView'),
    url(r'^profileView', views.profileView, name='profileView'),
    url(r'^viewBoard/(?P<id>\d+)/', views.viewBoard, name='viewBoard'),
    url(r'^viewPicture/(?P<id>\d+)/', views.viewPicture, name='viewPicture'),
    url(r'^editPicture/(?P<id>\d+)/', views.editPicture, name='editPicture'),
    url(r'^submitPicture/', views.submitPicture, name='submitPicture'),
    url(r'^deletePicture/(?P<id>\d+)/', views.deletePicture, name='deletePicture'),
    url(r'^editProfile', views.editProfile, name='editProfile')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
