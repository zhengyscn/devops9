"""devops9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# Application/users
from users.views import UserListV1
from users.views import UserListV2
from users.views import UserListV3
from users.views import UserListV4
from users.views import UserList5
from users.views import UserListView6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/v1', UserListV1),
    path('users/v2', UserListV2),
    path('users/v3', UserListV3),
    path('users/v4', UserListV4),
    path('users/v5', UserList5),
    path('users/v6', UserListView6.as_view()),
]
