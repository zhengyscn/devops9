
# 标准库
import json

# Django库
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import QueryDict
from django.contrib.auth import get_user_model
from django.views.generic import View


# 实例化settings.AUTH_USER_MODEL
User = get_user_model()



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
