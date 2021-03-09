from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from .models import *


class UserSerializers(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class UserAnotherCreateSerializers(ModelSerializer):
    UserBalance = ReadOnlyField()

    class Meta:
        model = UserAnotherConfig
        fields = '__all__'


class UserAnotherAnotherActionSerializers(UserAnotherCreateSerializers):
    user = UserSerializers(read_only=True)

    class Meta:
        model = UserAnotherConfig
        fields = '__all__'
