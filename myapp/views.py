from rest_framework.response import Response
from .models import User, UserProfile
from django.contrib.auth import logout
from rest_framework.authentication import authenticate
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class UserRegister(APIView):
    permission_classes = []

    def post(self, request):
        user_data = request.data
        email = user_data.get('email')
        password = user_data.get('password')
        password_confirm = user_data.get('password_confirm')
        profile_data = user_data.get('userprofile')

        if password_confirm != password:
            return Response({'error': 'passwords do not match'})

        User.objects.create_user(username=email, email=email, password=password)

        return Response({'msg': 'registration successful'})

class UserLogIn(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=email, email=email, password=password)

        if user is None:
            return Response({'error': 'wrong data', 'user': user})


        token = Token.objects.get_or_create(user=user)[0].key
        return Response({'token': token})


class UserLogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response('User Logged out successfully')
