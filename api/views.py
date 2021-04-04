
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,GenericAPIView,UpdateAPIView,ListAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializer import UserRegistrationSerializer,UserLoginSerializer,ShiftSerializer
from rest_framework import status
from .models import User,Shift
from datetimerange import DateTimeRange
from datetimerange import DateTimeRange
from datetime import datetime, time
# Create your views here.


class UserRegistrationView(CreateAPIView):
	
	serializer_class = UserRegistrationSerializer
	
	

	def post(self,request):
		serializer = self.serializer_class(data = request.data)
		serializer.is_valid(raise_exception =True)
		serializer.save()
		status_code = status.HTTP_201_CREATED
		response = {
			'success' : 'True',
			'status_code' : status_code,
			'message':'User Registered successfully',
		}

		return Response(response,status=status_code)


class UserLoginView(GenericAPIView):
	permission_classes =(AllowAny,)
	serializer_class = UserLoginSerializer
	model = User	

	def post(self,request):
		serializer = self.serializer_class(data = request.data)
		user = User.objects.get(email=request.data['email'])
		serializer.is_valid(raise_exception =True)
		print(user.is_staff)
		status_code = status.HTTP_200_OK
		response = {
			'success' : 'True',
			'status_code' : status_code,
			'message':'User Logged in successfully',
			'token' : serializer.data['token']
		}

		return Response(response,status=status_code,)

class ShiftAdd(CreateAPIView):
    serializer_class = ShiftSerializer
    model = Shift
    # permission_classes=[IsAuthenticated]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'status':'success'})
	