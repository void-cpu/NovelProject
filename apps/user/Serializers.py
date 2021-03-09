from rest_framework.serializers import ModelSerializer, ReadOnlyField, HyperlinkedModelSerializer

from .models import *


class UserSerializers(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserReadOnlySerializers(ReadOnlyField):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserAnotherSerializers(ModelSerializer):
    user = UserReadOnlySerializers(read_only=True)

    class Meta:
        model = UserAnotherConfig
        fields = '__all__'
