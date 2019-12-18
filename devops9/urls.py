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
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# Application/users
from users.views import UserListV1
from users.views import UserListV2
from users.views import UserListV3
from users.views import UserListV4
from users.views import UserList5
from users.views import UserListView6
from users.authviews import CustomAuthToken

# Application/books
from books.views import PublishApiView
from books.views import PublishGenericApiView
from books.views import PublishMixinsGenericApiView
from books.views import PublishListCreateRetrieveUpdateDestroyApiView
from books.views import PublishxApiViewSets1
from books.views import PublishxApiViewSets2
from books.views import PublishxApiViewSets3
from books.views import BookApiViewSets1



route = DefaultRouter()
route.register(r"api/v1/books", PublishxApiViewSets2)
route.register(r"api/v2/books", PublishxApiViewSets3)
route.register(r"api/v3/books", BookApiViewSets1)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='My API title')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/v1', UserListV1),
    path('users/v2', UserListV2),
    path('users/v3', UserListV3),
    path('users/v4', UserListV4),
    path('users/v5', UserList5),
    path('users/v6', UserListView6.as_view()),

    path('books/publish/v1', PublishApiView.as_view()),
    path('books/publish/v1/<int:pk>', PublishApiView.as_view()),
    path('books/publish/v2', PublishGenericApiView.as_view()),
    path('books/publish/v2/<int:pk>', PublishGenericApiView.as_view()),
    path('books/publish/v3', PublishMixinsGenericApiView.as_view()),
    path('books/publish/v3/<int:pk>', PublishMixinsGenericApiView.as_view()),
    path('books/publish/v4', PublishListCreateRetrieveUpdateDestroyApiView.as_view()),
    path('books/publish/v4/<int:pk>', PublishListCreateRetrieveUpdateDestroyApiView.as_view()),
    path('books/publish/v5/', PublishxApiViewSets1.as_view(
        {"get" : "list", "post" : "create"}
    )),
    path('books/publish/v5/<int:pk>', PublishxApiViewSets1.as_view(
        {"get" : "retrieve", "put" : "update", "delete" : "destroy"}
    )),

    path('books/publish/v6/', PublishxApiViewSets2.as_view(
        {"get" : "list", "post" : "create"}
    )),
    path('books/publish/v6/<int:pk>', PublishxApiViewSets2.as_view(
        {"get" : "retrieve", "put" : "update", "delete" : "destroy"}
    )),

]

urlpatterns += [
    path('api-token-auth/v1', views.obtain_auth_token),
    path('api-token-auth/v2', CustomAuthToken.as_view()),
]

urlpatterns += route.urls