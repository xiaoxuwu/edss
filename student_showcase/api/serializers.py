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

class StudentSerializer(serializers.ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Student
        fields = ('account', 'major', 'year', 'membership', 'clearance', 'resume', 'linked_in', 'attendance')

    def create(self, validated_data):
        account = validated_data.pop('account')
        user = User.objects.create(**account)
        student = Student.objects.create(account=user, **validated_data)
        return student;
