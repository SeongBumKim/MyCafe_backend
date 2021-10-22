from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from login.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def login_view(request):
    # deserializer = UserSerializer(request.data)
    # email = deserializer.data['email']
    # password = deserializer.data['password']
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)

    if user is not None: #user가 not None(true)면 밑에 조건
        login(request, user)
        return Response({'username': username})

    return Response({'error': 'login failed'})

@api_view(['GET'])
def logout_view(request):
     logout(request)
     return Response({'message': 'logout success'})

@api_view(['GET'])
def user_list(request):
   users = User.objects.all()
   print(users)
   serializer = UserSerializer(users, many=True)
   return Response(serializer.data)