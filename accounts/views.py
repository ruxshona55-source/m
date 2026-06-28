

from accounts import serializers
# from accounts.jwt_utils import create_tokens
from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status, permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, permission_classes
from accounts.serializers import LoginSerializer, UserSerializer, UserCreateSerializers
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from rest_framework.status import HTTP_200_OK


# action qachon ishlatamiz qachonki get,put,patch,create,delete dan boshqa narsa yozsak ishlatiladi



class AuthViewSet(viewsets.GenericViewSet,CreateModelMixin):
    queryset = User.objects.all()
    serializer_class=UserCreateSerializers
    # permission_classes = [permissions.AllowAny]
    def get_permissions(self):
        if self.action in ('logout_user','get_session'):
            return [permissions.IsAuthenticated]
        return [permissions.AllowAny()]

    # @action(methods=['post'],detail=False,url_path='login',serializer_class=LoginSerializer)
# detail=False(true->aynan osha obektga kirsa,pk kere bolsa)
#     def login_user(self,request):
#         serializer=LoginSerializer(data=request.data)
#         if serializer.is_valid():
#            user=serializer.validated_data['user']
#            login(request,user)
#            return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def login_user(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


    @action(methods=['delete'],detail=False,url_path='logout')
    def logout_user(self,request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(methods=['get'],detail=False,url_path='session',serializer_class=UserSerializer)
    def get_session(self,request):
        user=request.user
        return Response(UserSerializer(user).data,status=status.HTTP_200_OK)
#
# class CustomJWTViewSet(viewsets.GenericViewSet):
#     @action(methods=['post'],detail=False,serializer_class=LoginSerializer,url_path='login_jwt')
#     def login_jwt(self,request):
#         username=request.data.get('username')
#         password=request.data.get('password')
#         user=authenticate(username=username,password=password)
#         if user:
#             tokens=create_tokens(user.id)
#             return Response({'tokens':tokens},status=status.HTTP_200_OK)
#         return Response({'error':'user error'},status=status.HTTP_400_BAD_REQUEST)

    # @action(methods=['post'], detail=False, serializer_class=LoginSerializer, url_path='refresh')


# class AuthWithTokenViewSet(viewsets.GenericViewSet):


from rest_framework.authtoken.models import Token

class AuthWithTokenViewSet(viewsets.GenericViewSet):

    def get_permissions(self):
        if self.action in ['logout', 'session']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})

    @action(methods=['post'], detail=False)
    def logout(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response({"message": "Logged out"})

    @action(methods=['get'], detail=False)
    def session(self, request):
        return Response(UserSerializer(request.user).data)




