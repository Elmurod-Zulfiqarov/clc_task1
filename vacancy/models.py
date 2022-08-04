from tkinter import CASCADE
from django.db import models

from common.models import User
from helpers.models import BaseModel


class Worker(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="worker")
    exprience = models.TextField(null=True, blank=True)
    from_salary = models.IntegerField()
    to_salary = models.IntegerField()


class Company(BaseModel):
    title = models.CharField(max_length=128)
    content = models.TextField(null=True, blank=True)


class Category(BaseModel):
    title = models.CharField(max_length=128)


class Vacancy(BaseModel):
    title = models.CharField(max_length=128)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category")
