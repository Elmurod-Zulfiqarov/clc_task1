from rest_framework.serializers import ModelSerializer
from .models import Worker, Company, Category, Vacancy


class WorkerSerializer(ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class VacancySerializer(ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'
