from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView, Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

class ProductAPIView(APIView) :
    def get(self, request) :
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        print(serializers)
        return Response(serializers.data)
    
    def post(self, request) :
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)