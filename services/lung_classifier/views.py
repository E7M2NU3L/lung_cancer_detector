from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from services.lung_classifier.models import CovidModel, LungCancerModel, LungCancerCtModel
from rest_framework import status
from rest_framework.response import Response
from services.lung_classifier.serializers import CovidSerializer, LungCancerCTSerializer, LungCancerSerializer
from services.lung_classifier.utilities.cancer_api import LungCancerPredictor

class CovidChecker(APIView):
    def get_object(self, pk):
        try:
            return CovidModel.objects.get(pk=pk)
        except CovidModel.DoesNotExist:
            raise HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CovidSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CovidSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, format=None):
        serializer = CovidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LungCancerChecker(APIView):
    def get_object(self, pk):
        try:
            return LungCancerModel.objects.get(pk=pk)
        except LungCancerModel.DoesNotExist:
            raise HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LungCancerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LungCancerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, format=None):
        serializer = LungCancerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LungCancerCTCheck(APIView):
    def get_object(self, pk):
        try:
            return LungCancerCtModel.objects.get(pk=pk)
        except LungCancerCtModel.DoesNotExist:
            raise HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LungCancerCTSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LungCancerCTSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, format=None):
        serializer = LungCancerCTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)