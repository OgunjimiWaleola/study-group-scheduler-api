from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if User.objects.filter(username=data['username']).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)