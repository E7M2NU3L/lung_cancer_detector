from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from lung_classifier.models import CovidModel, LungCancerModel, LungCancerCtModel
from rest_framework import status
from rest_framework.response import Response
from lung_classifier.serializers import CovidSerializer, LungCancerCTSerializer, LungCancerSerializer
from lung_classifier.utilities.cancer_api import LungCancerPredictor, LungCancerCTPredictor
from lung_classifier.utilities.covid_api import CovidPredictor

class CovidChecker(APIView):
    def get_object(self, pk):
        try:
            return CovidModel.objects.get(pk=pk)
        except CovidModel.DoesNotExist:
            raise HTTP_404_NOT_FOUND
        
    def get(self, request, format=None):
        snippet = CovidModel.objects.all()
        return Response(snippet)

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
        request_data = request.data
        print(request_data)
        image_url = request_data.get('image_url')
        print(image_url)
        
        response = CovidPredictor(image=image_url)
        output = response.predict_image()
        print(output)

        request_data['output'] = output
        serializer = CovidSerializer(data=request_data)
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

    def get(self, request, format=None):
        snippet = LungCancerModel.objects.all()
        return Response(snippet)

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
        input_data = request.data
        responses = LungCancerPredictor(data=input_data).predict()
        input_data['lung_cancer'] = responses
        print(input_data)
        serializer = LungCancerSerializer(data=input_data)
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
        request_data = request.data
        print(request_data)
        image_url = request_data.get('image_url')
        print(image_url)
        
        response = LungCancerCTPredictor(image=image_url)
        output = response.predict_image()
        print(output)

        request_data['output'] = output
        serializer = LungCancerCTSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)