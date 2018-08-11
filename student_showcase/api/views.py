# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from api.models import *
from api.serializers import *
import pdb

@api_view(['GET'])
def api_root(request, format=None):
    return JsonResponse({
    'api/': 'Access EDSS API.',
    'admin/': 'Access EDSS API admin panel.',
    'auth/': 'Authenticatication for EDSS API.',
    }, status=200)

class CompanyViewSet(viewsets.ModelViewSet):
    """
    RESTful API endpoint for Company
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request):
        serializer = CompanyAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        request.data['password'] = '*' * len(request.data['password'])
        return JsonResponse({'request': request.data, 'status': 'created successfully'}, status=201)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentAccountSerializer

    def post(self, request):
        new_user = {
            "username": request.data['username'],
            "password": request.data['password'],
            "email": request.data['email'],
            "first_name": request.data['first_name'],
            "last_name": request.data['last_name'],
            "student_data": request.data['student_data'],
        }
        serializer_class.create(new_user)
        return Response(serializer_class(new_user).data)

    def put(self, request):
        try:
            user = Student.object.get(request.data['id'])
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if "username" in request.data:
            user.username = request.data['username']
        if "password" in request.data:
            user.password = request.data['password']
        if "email" in request.data:
            user.email = request.data['email']
        if "first_name" in request.data:
            user.first_name = request.data['first_name']
        if "last_name" in request.data:
            user.last_name = request.data['last_name']
        if "student_data" in request.data:
            user.student_data = request.data['student_data']
        return Response(serializer_class(user).data)

    def get(self, request):
        try:
            user = Student.object.get(request.data['id'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return user



# class StudentAccountViewSet(viewsets.ModelViewSet):
#     queryset = StudentAccount.objects.all()
#     serializer_class = StudentAccountSerializer
