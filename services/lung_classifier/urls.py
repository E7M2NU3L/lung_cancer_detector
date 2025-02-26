from django.urls import path
from lung_classifier import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('covid-check', views.CovidChecker.as_view()),
    path('cancer-check', views.LungCancerChecker.as_view()),
    path('cancer-check-ct', views.LungCancerCTCheck.as_view()),

    path('covid-check/<int:pk>', views.CovidCheckSingle.as_view()),
    path('cancer-check/<int:pk>', views.LungCancerSingle.as_view()),
    path('cancer-check-ct/<int:pk>', views.LungCancerCTSingle.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)