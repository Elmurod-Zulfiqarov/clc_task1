from django.urls import path
from .views import VacansyView

urlpatterns = [
    path("", VacansyView.as_view, name="vacancy")
]
