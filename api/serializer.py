from .models import User,Shift
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings


class UserRegistrationSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email','password','is_staff','id')
		read_only_fields = ('is_active', 'last_login', 'groups', 'user_permissions', 'is_superuser',
                            'last_update_userid', 'last_update_date')
		extra_kwargs = {
            'password': {'write_only': True},}

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)		
		return user	

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self,data):
        email = data.get("email",None)
        password =data.get("password",None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('user not found')
        
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
        
        except User.DoesNotExist:
            raise serializers.ValidationError(
				'User with given email and password does not exist')
        
        return {
		'email': user.email,
		'token': jwt_token
		}



class ShiftSerializer(serializers.ModelSerializer):

	class Meta:
		model = Shift
		fields = '__all__'
