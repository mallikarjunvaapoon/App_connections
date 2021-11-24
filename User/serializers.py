from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=30, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def validate(self, attrs):
            email = attrs.get('email','')
            username = attrs.get('username', '')

            if not username.isalnum():
                raise serializers.ValidationError('username should be string ')
            return attrs

        def create(self, validate_data):
            return User.objects.create_user(**validate_data)

