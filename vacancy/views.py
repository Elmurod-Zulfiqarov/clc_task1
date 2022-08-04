from rest_framework.generics import ListCreateAPIView
from .models import Vacancy
from .serializers import VacancySerializer


class VacansyView(ListCreateAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()
