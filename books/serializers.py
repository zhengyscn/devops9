from rest_framework import serializers


from .models import Publish
from .models import Author
from .models import Book






class PublishSerializer(serializers.ModelSerializer):

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

    #
    def to_author_response(self, instance):
        retdata = []
        print(instance)
        return retdata

    def to_representation(self, instance):
        pass


