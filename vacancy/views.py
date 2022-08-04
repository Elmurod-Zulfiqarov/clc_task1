from rest_framework.generics import ListAPIView
from .models import Vacancy, Category
from .serializers import CategorySerializer, VacancySerializer
from django.db import models


class VacansyView(ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.annotate(
            vacancy_count=models.Count('vacancy'),
            company_count=models.Count('company'),
            worker_count=models.Count("worker"),
        )


class CategoryView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.aggregate(models.Count("worker_category"))
