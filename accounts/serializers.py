from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'confirm_password', 'full_name', 
                  'sex', 'phone_number', 'country')
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        try:
            user = CustomUser.objects.get(email=validated_data['email'], is_active=False)
        except:
            user = CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'],
                                              full_name=validated_data['full_name'], sex=validated_data['sex'],
                                              phone_number=validated_data['phone_number'], country=validated_data['country'])

        return user 
        


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        return user
        