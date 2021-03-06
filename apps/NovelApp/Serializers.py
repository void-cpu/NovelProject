from rest_framework.serializers import ModelSerializer, ReadOnlyField, HyperlinkedModelSerializer

from .models import *


class AuthorSerializers(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class NovelClassSerializers(ModelSerializer):
    class Meta:
        model = NovelClass
        fields = '__all__'


class NovelSerializers(ModelSerializer):
    class Meta:
        model = Novel
        fields = '__all__'


class InfoSerializers(ModelSerializer):
    words = ReadOnlyField(read_only=True)

    class Meta:
        model = Info
        fields = '__all__'


class ChapterSerializers(ModelSerializer):

    class Meta:
        model = Chapter
        fields = '__all__'
