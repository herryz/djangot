from rest_framework import serializers
from models import WechatUser
from django.contrib.auth.models import User


class WechatUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WechatUser
        fields = ('openid', 'unionid', 'name')


class UserSerializer(serializers.ModelSerializer):
    wechatuser = serializers.PrimaryKeyRelatedField(many=True, queryset=WechatUser.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'wechatuser')