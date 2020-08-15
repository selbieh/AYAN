from .serializers import SignUpSerializer
from rest_framework.generics import CreateAPIView
from  rest_framework.views import APIView
from .models import Users
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    def post(self, request, *args, **kwargs):
        data=request.data
        validatedUser=SignUpSerializer(data=data)
        if validatedUser.is_valid():
            Users.objects.create_user(**validatedUser.validated_data)
            return Response({'status':'created','user':validatedUser.data})
        else:
            return Response(validatedUser.errors,status=status.HTTP_400_BAD_REQUEST)


class CustomLogIn(APIView):
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        if email and password:
            user = authenticate(request,username=email, password=password)
            if user :
                token, created = Token.objects.get_or_create(user=user)
                return Response({'Token':token.key})
            else:
                return Response({'token': 'wrong email or password '},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"email or password missing"},status=status.HTTP_400_BAD_REQUEST)