from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from .serializers3 import PublishSerializer
from .models import Publish



class PublishApiView(APIView):
    '''
    GET     : 获取数据列表
    POST    ：提交数据
    PUT     : 修改数据
    DELETE  : 删除数据
    '''
    MODEL_CLASS = Publish
    SERIALIZER_CLASS = PublishSerializer

    def get_object(self, pk):
        try:
            return self.MODEL_CLASS.objects.get(pk=pk)
        except self.MODEL_CLASS.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        # 序列化
        print("request: ", request.data, type(request.data))
        print('args: ', args)
        print('kwargs: ', kwargs)


        pk = kwargs.get('pk', None)
        if not pk:
            queryset = self.MODEL_CLASS.objects.all()
            s = self.SERIALIZER_CLASS(queryset, many=True)
        else:
            instance = self.get_object(pk)
            s = self.SERIALIZER_CLASS(instance)
        return Response(s.data)

    def post(self, request, *args, **kwargs):
        # 反序列化
        print("request: ", request.data, type(request.data))
        print('args: ', args)
        print('kwargs: ', kwargs)

        s = self.SERIALIZER_CLASS(data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
        return Response(s.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = self.get_object(pk)
        s = self.SERIALIZER_CLASS(instance, request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
        return Response(s.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        instance = self.get_object(pk)
        instance.delete()
        return Response("delete is ok", status=status.HTTP_200_OK)


class PublishGenericApiView(GenericAPIView):
    MODEL_CLASS = Publish
    queryset = MODEL_CLASS.objects.all()
    serializer_class = PublishSerializer

    def get_queryset(self):
        _queryset = super(PublishGenericApiView, self).get_queryset()
        print(self.request.data)
        print(_queryset)
        keyword = self.request.GET.get('keyword', None)
        if keyword:
            _queryset = _queryset.filter(name__icontains=keyword.strip())
        return _queryset


    def get(self, request, *args, **kwargs):
        if kwargs.get(self.lookup_field):
            instance = self.get_object()
            s = self.get_serializer(instance)
        else:
            instances = self.get_queryset()
            s = self.get_serializer(instances, many=True)
        return Response(s.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        s = self.get_serializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
        return Response(s.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        s = self.get_serializer(instance, request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
        return Response(s.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response("delete is ok", status=status.HTTP_200_OK)


class PublishMixinsGenericApiView(mixins.ListModelMixin,
                                  mixins.CreateModelMixin,
                                  mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  GenericAPIView):
    MODEL_CLASS = Publish
    queryset = MODEL_CLASS.objects.all()
    serializer_class = PublishSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get(self.lookup_field, None)
        if pk:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 单查询拆分
class PublishListCreateRetrieveUpdateDestroyApiView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    MODEL_CLASS = Publish
    queryset = MODEL_CLASS.objects.all()
    serializer_class = PublishSerializer


# 等价于PublishxApiViewSets2
class PublishxApiViewSets1(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    MODEL_CLASS = Publish
    queryset = MODEL_CLASS.objects.all()
    serializer_class = PublishSerializer


# PublishxApiViewSets1
class PublishxApiViewSets2(viewsets.ModelViewSet):
    MODEL_CLASS = Publish
    queryset = MODEL_CLASS.objects.all()
    serializer_class = PublishSerializer


class PublishxApiViewSets3(viewsets.ModelViewSet):
    MODEL_CLASS = Publish
    queryset = MODEL_CLASS.objects.all()
    serializer_class = PublishSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]