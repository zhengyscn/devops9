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




class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    #
    def to_author_response(self, instance):
        retdata = []
        print(instance)
        return retdata

    def to_representation(self, instance):
        pass


