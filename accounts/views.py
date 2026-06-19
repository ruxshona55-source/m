

from accounts import serializers
from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, permission_classes
from accounts.serializers import LoginSerializer, UserSerializer, UserCreateSerializers
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response


# action qachon ishlatamiz qachonki get,put,patch,create,delete dan boshqa narsa yozsak ishlatiladi



class AuthViewSet(viewsets.GenericViewSet,CreateModelMixin):
    queryset = User.objects.all()
    serializer_class=UserCreateSerializers
    # permission_classes = [permissions.AllowAny]
    def get_permissions(self):
        if self.action in ('logout_user','get_session'):
            return [permissions.IsAuthenticated]
        return [permissions.AllowAny()]

    @action(methods=['post'],detail=False,url_path='login',serializer_class=LoginSerializer)
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


