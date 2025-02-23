from django.urls import path
from lung_classifier import views

urlpatterns = [
    path('covid-check', views.CovidChecker.as_view()),
    path('cancer-check', views.LungCancerChecker.as_view()),
    path('cancer-check-ct', views.LungCancerCTCheck.as_view())
]