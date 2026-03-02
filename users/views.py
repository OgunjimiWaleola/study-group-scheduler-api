from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token



class RegisterView(APIView):
    permission_classes = [AllowAny]  # anyone can register

    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user)
        return Response({"message": "User created", "token": token.key})

class LoginView(APIView):
    permission_classes = [AllowAny]  # anyone can login

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", "token": token.key})