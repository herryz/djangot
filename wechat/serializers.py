from rest_framework import serializers
from wechat.models import WechatUser, Comment
from django.contrib.auth.models import User


class WechatUserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WechatUser
        fields = ('openid', 'unionid', 'name', 'owner')


class UserSerializer(serializers.ModelSerializer):
    wechatuser = serializers.PrimaryKeyRelatedField(many=True, queryset=WechatUser.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'wechatuser')


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()