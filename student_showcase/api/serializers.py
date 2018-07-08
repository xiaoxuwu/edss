from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class CompanySerializer(serializers.ModelSerializer):
    rep = UserSerializer()

    class Meta:
        model = Company
        fields = '__all__'

class CompanyAccountSerializer(serializers.ModelSerializer):
    company_data = CompanySerializer()

    class Meta:
        model = User
        fields =  ('username', 'password', 'email', 'first_name', 'last_name', 'company_data')

    def create(self, validated_data):
        company_data = validated_data.pop('company_data')
        user = User.objects.create(**validated_data)
        Company.objects.create(rep=user, **company_data)
        return user
