from django.urls import path
from services.lung_classifier import views

utlpatterns = [
    path('covid-check', views.CovidChecker.as_view()),
    path('cancer-check', views.LungCancerChecker.as_view()),
    path('cancer-check-ct', views.LungCancerCTCheck.as_view())
]