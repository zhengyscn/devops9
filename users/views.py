
# 标准库
import json

# Django库
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import QueryDict
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.contrib.auth.models import Group, Permission
# 第三方过滤器
from django_filters import rest_framework as dj_filters

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response


# DRF内置过滤器
from rest_framework import filters

# 自定义
from .serializers import PermissionSerializer
from .serializers import GroupSerializer
from .serializers import UserSerializer

from .filters import PermissionFilter
from utils.pagination import CustomPagination


# 实例化settings.AUTH_USER_MODEL
User = get_user_model()



class UserViewSet1(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['=username', '=phone']
    ordering_fields = ('id', )


class PermissionViewSet1(viewsets.ReadOnlyModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['=name', '=codename']
    ordering_fields = ('id', )


class PermissionViewSet2(viewsets.ReadOnlyModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_class = PermissionFilter
    search_fields = ['=name', '=codename']
    ordering_fields = ('id', )



class PermissionViewSet3(viewsets.ReadOnlyModelViewSet):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = CustomPagination
    filter_backends = (dj_filters.DjangoFilterBackend, )
    filterset_fields = ('name', 'codename')
    ordering_fields = ('id', )


class GroupViewSet1(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination
    # filter_backends = (dj_filters.DjangoFilterBackend, )
    # filterset_fields = ('name', 'codename')
    # ordering_fields = ('id', )


class UserPermissionGroupViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = User.objects.all()

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        group_ids = data.get('group_ids', None)
        permission_ids = data.get('permission_ids', None)
        if group_ids:
            u = self.get_object()
            u.groups.set(group_ids)
            return Response(data="partial_update success.", status=status.HTTP_200_OK)
        elif permission_ids:
            u = self.get_object()
            u.user_permissions.set(permission_ids)
            return Response(data="partial_update success.", status=status.HTTP_200_OK)
        return Response(data='NO_CONTENT', status=status.HTTP_204_NO_CONTENT)


class UserPermissionViewSet1(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = User.objects.all()

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        ids = data.get('ids', None)
        if ids:
            u = self.get_object()
            u.groups.set(ids)
            return Response(data=None, status=status.HTTP_200_OK)
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


class GroupPermissionViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):

    queryset = Group.objects.all()

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.data)


        return super(GroupPermissionViewSet, self).partial_update(request, *args, **kwargs)


def UserListV1(request, *args, **kwargs):
    users = User.objects.all()
    print(users, type(users))
    return HttpResponse(users)


def UserListV2(request, *args, **kwargs):
    users = User.objects.all()
    retdata = []
    for u in users:
        retdata.append({
            'id' : u.pk,
            'username' : u.username,
            'phone' : u.phone
        })
    return HttpResponse(json.dumps(retdata), content_type='application/json')


def UserListV3(request, *args, **kwargs):
    users = User.objects.all()
    retdata = []
    for u in users:
        retdata.append({
            'id' : u.pk,
            'username' : u.username,
            'phone' : u.phone
        })
    return JsonResponse(retdata, safe=False)



def UserListV4(request, *args, **kwargs):
    users = User.objects.all()
    data = serializers.serialize("json", users)
    retdata = json.loads(data)
    return JsonResponse(retdata, safe=False)


def UserList5(request, *args, **kwargs):
    print('method', request.method)
    print('META', request.META)

    if request.method == 'GET':
        users = User.objects.all()
        data = serializers.serialize("json", users)
        retdata = json.loads(data)
        return JsonResponse(retdata, safe=False)

    elif request.method == 'POST':
        print(request.body)
        print(request.POST)
        print(dict(request.POST))
        print(type(dict(request.POST)))

        return JsonResponse("POST is ok.", safe=True)

    elif request.method == 'PUT':
        print(request.body)
        data = QueryDict(request.body).dict()
        print(data)
        return JsonResponse("PUT is ok.", safe=True)

    elif request.method == 'DELETE':
        print(request.body)
        data = QueryDict(request.body).dict()
        print(data)
        return JsonResponse("DELETE is ok.", safe=True)

    else:
        return JsonResponse("Method not found.", safe=True)


class UserListView6(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse('GET is ok', safe=False)

    def post(self, request, *args, **kwargs):
        return JsonResponse("POST is ok.", safe=True)

    def put(self, request, *args, **kwargs):
        return JsonResponse("PUT is ok.", safe=True)

    def delete(self, request, *args, **kwargs):
        return JsonResponse("DELETE is ok.", safe=True)

    def patch(self, request, *args, **kwargs):
        return JsonResponse("patch is ok.", safe=True)
