from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from .utility import Utility
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()


            user = User.objects.get(email=serializer.data['email'])

            token = RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain

            relativeLink = reverse('email')

            absurl = 'http://'+current_site+relativeLink+"?token ="+ str(token)
            email_body = "hi"+user.username+'use the below link to verify your email \n' + absurl

            data = {'email_body':email_body, 'to_email':[user.email], 'email_subject':'verify your email'}

            Utility.send_email(data)





            return Response(serializer.data, status= status.HTTP_201_CREATED)

class Verify_Email(generics.GenericAPIView):
    def get(self):
        pass


class LoginView(generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username = username).first()
        password = User.objects.filter(password=password).first()

        if user is None:
            raise AuthenticationFailed('user not defined')

        return Response({
            "message": "success"
        })
