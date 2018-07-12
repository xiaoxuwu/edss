# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
class Company(models.Model):
    SPACES = (
        ("P", "Patio Exhibition"),
        ("PS_2", "Premium Space, 2 Tables"),
        ("PS_1", "Premium Space, 1 Table"),
        ("SS_2", "Standard Space, 2 Tables"),
        ("SS_1", "Standard Space, 1 Table"),
    )
    DESIRED_POSITION_TYPES = (
        ("IN", "Interns"),
        ("FT", "Full-time"),
        ("B", "Both")
    )

    company_name = models.CharField(max_length=30)
    company_description = models.TextField()
    rep = models.OneToOneField(User, on_delete=models.CASCADE)
    rep_phone = models.CharField(max_length=12)
    space = models.CharField(max_length=4, choices=SPACES)
    looking_for = models.CharField(max_length=2, choices=DESIRED_POSITION_TYPES)
    special_needs = models.TextField(blank=True)

    def __str__(self):
        return self.company_name

class Student(models.Model):
    YEARS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    )

    account = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=30)
    # on frontend, have pulldown with engineering majors, option to type in other if needed
    year = models.CharField(max_length=1, choices=YEARS)

    membership = models.PositiveSmallIntegerField(default=0)
    # bit-wise OR the clubs you are in
    # 1 - TBP
    # 2 - HKN
    # 4 - XE
    # 8 - UPE
    # ... (can add more)

    clearance = models.BooleanField(default=False)
    resume = models.FileField(upload_to='resumes/')

    linked_in = models.CharField(max_length=50, blank=true)
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return self.account
        #User __str__ defaults to username