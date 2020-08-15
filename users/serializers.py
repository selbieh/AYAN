from rest_framework.serializers import ModelSerializer
from .models import Users



class SignUpSerializer(ModelSerializer):
    class Meta:
        model=Users
        fields=['email','password']