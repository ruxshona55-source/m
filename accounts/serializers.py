from django.contrib.auth import authenticate

from rest_framework import serializers
from accounts.models import User
class UserCreateSerializers(serializers.ModelSerializer):
    re_password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password','re_password']
        extra_kwargs={'password':{'write_only':True}}
    #     passwordni userga korsatmaslik uchun -> {'write_only':True}
    def validate(self, data):
        password=data.get('password')
        re_password=data.pop('re_password')

        if password != re_password:
            raise serializers.ValidationError("password re_password bilan birxil emas")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
# passwordni hashlab berish uchun-> User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name']

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    def validated(self,data):
        username = data.get['username']
        password = data.get['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("username yoki password xato")
        return {"user":user}
