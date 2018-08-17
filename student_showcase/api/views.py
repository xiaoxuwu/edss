# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import permissions
from rest_framework.decorators import api_view, action
from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from api.models import *
from api.serializers import *
from api.permissions import *
import pdb
import io
import os
import zipfile
from django.conf import settings

@api_view(['GET'])
def api_root(request, format=None):
    return JsonResponse({
    'api/': 'Access EDSS API.',
    'admin/': 'Access EDSS API admin panel.',
    'auth/': 'Authenticatication for EDSS API.',
    }, status=200)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [ViewAllPermissions]
        elif self.action == 'resumes':
            permission_classes = [ViewAllPermissions]
        elif self.action == 'retrieve':
            permission_classes = [StudentPermissions]
        elif self.action == 'resume':
            permission_classes = [StudentPermissions]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]


    # def post(self, request):
    #     new_user = request.data['student_data']
    #     new_user['account'] = request.data['account']
    #     return serializer_class.create(new_user)
    #
    # def put(self, request):
    #     try:
    #         user = Student.objects.get(account_id=request.data['id'])
    #     except Student.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     if "account" in request.data:
    #         user.account = request.data['account']
    #     if "major" in request.data:
    #         user.major = request.data['major']
    #     if "year" in request.data:
    #         user.year = request.data['year']
    #     if "membership" in request.data:
    #         user.membership = request.data['membership']
    #     if "clearance" in request.data:
    #         user.clearance = request.data['clearance']
    #     if "resume" in request.data:
    #         user.resume = request.data['resume']
    #     if "linked_in" in request.data:
    #         user.linked_in = request.data['linked_in']
    #     if "attendance" in request.data:
    #         user.attendance = request.data['attendance']
    #     return user

    @action(detail=True)
    def resume(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            self.check_object_permissions(request, student)
            print(student)
            file = student.resume
            name = student.account.last_name
            response = HttpResponse(content=file)
            response['Content-Type'] = 'application/pdf'
            response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % name
            return response
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False)
    def resumes(self, request):
        students = Student.objects.all()
        b = io.BytesIO()
        zf = zipfile.ZipFile(b, 'w')
        for student in students:
            zf.write(student.resume.path, student.resume.name)
        zf.close()

        response = HttpResponse(content=b.getvalue());
        response['Content-Type'] = 'application/x-zip-compressed'
        response['Content-Disposition'] = 'attachment; filename="%s.zip"' % "resumes"
        return response
