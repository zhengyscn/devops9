from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission


# 实例化settings.AUTH_USER_MODEL
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'phone', 'email', 'password', 'is_active')
        extra_kwargs = {
            'password' : {
                'write_only' : True,
            }
        }

    def to_representation(self, instance):
        representation_data = super(UserSerializer, self).to_representation(instance)
        groups = []
        for g in instance.groups.all():
            groups.append({
                'id'    : g.pk,
                'name'  : g.name,
            })

        permissions = []
        for p in instance.user_permissions.all():
            permissions.append({
                'id'    : p.pk,
                'name'  : p.name,
                'codename'  : p.codename,
            })

        representation_data['groups'] = groups
        representation_data['permissions'] = permissions
        return representation_data

    def create(self, validated_data):
        instance = super(UserSerializer, self).create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super(UserSerializer, self).update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance



'''
    外键在哪定义，谁是正查，否则反查。
'''

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        # fields = '__all__'
        fields = ('id', 'name', )

    def to_representation(self, instance):
        representation_data = super(GroupSerializer, self).to_representation(instance)

        permissions = []
        for p in instance.permissions.all():
            permissions.append({
                'id'    : p.pk,
                'name'  : p.name,
                'codename': p.codename,
            })
        representation_data['permissions'] = permissions

        return representation_data


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')