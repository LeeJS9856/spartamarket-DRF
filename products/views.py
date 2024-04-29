from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Response
from .serializers import ProductSerializer
from .models import Product

class ProductAPIView(APIView) :
    def get(self, request) :
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        print(serializers)
        return Response(serializers.data)