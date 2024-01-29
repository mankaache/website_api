from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    password_confirmation = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    def validate_password_confirmation(self, value):
        password = self.get_initial().get('password')
        if password != value:
            raise serializers.ValidationError(_('Passwords do not match'))
        return value

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password_confirmation']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)