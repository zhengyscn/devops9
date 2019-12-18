from rest_framework import serializers


from .models import Publish
from .models import Author
from .models import Book








class PublishSerializer(serializers.Serializer):

    id      =   serializers.IntegerField(required=False)
    name    =   serializers.CharField(max_length=32, required=True)
    city    =   serializers.CharField(max_length=32, required=True)
    address =   serializers.CharField(max_length=32, required=True)


    # Post
    def create(self, validated_data):
        print("validated_data", validated_data)
        return Publish.objects.create(**validated_data)

    # Put
    def update(self, instance, validated_data):
        print("instance", instance)
        print("validated_data", validated_data)
        instance.name = validated_data['name']
        instance.city = validated_data['city']
        instance.address = validated_data['address']
        instance.save()
        return instance

    # def validate(self, data):
    #     '''
    #     对象(表)级别验证
    #     如果要对多个字段进行验证
    #     :param data:
    #     :return:
    #     '''
    #     if data['city'] != ['beijing', 'zhengzhou']:
    #         raise serializers.ValidationError("City validate error.")
    #     return data
    #
    # def validate_city(self, value):
    #     '''
    #     字段级别验证
    #     validate_<field_name>，
    #     如果参数中声明required=False，则跳过这个验证.
    #     :return:
    #     '''
    #     if value not in value.lower():
    #         raise serializers.ValidationError("Value is lower.")
    #     return value


# 针对ModelSerializer序列化
class PublishModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publish
        fields = '__all__'




class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


    def to_representation(self, instance):
        '''
        关联表输出json数据
        :param instance:
        :return:
        '''
        representation = super(BookSerializer, self).to_representation(instance)

        publisher = instance.publisher
        representation['publisher'] = {
            'id'        :   publisher.pk,
            'name'      :   publisher.name,
            'address'   :   publisher.address,
        }

        for u in instance.author.all():
            if u:
                representation['author'].append({
                    'id'    : u.id,
                    'name'  : u.name,
                    'email' : u.email
                })
        return representation



    def to_internal_value(self, data):
        '''
        通过关联表的铸剑自动关联
        前端到后端序列化
        :param data:
        :return:
        '''
        print(data)
        return super(BookSerializer, self).to_internal_value(data)




