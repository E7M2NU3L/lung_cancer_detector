from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

@api_view(['GET', 'POST'])
def health_check(request):
    return Response({
        "status" : True,
        "message" : "App is running perfectly"
    }, status=HTTP_200_OK)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/classifiers/', include('lung_classifier.urls')),
    path('', health_check)
]
