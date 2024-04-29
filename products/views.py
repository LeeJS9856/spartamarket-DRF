from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView, Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ProductSerializer, ProductDetailSerializer
from .models import Product

class ProductAPIView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request) :
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)
    
    def post(self, request) :
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(author = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def dispatch(self, request):
        if request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return super().dispatch(request)
        
class ProductDetailAPIView(APIView) :
    permission_classes = [IsAuthenticated]
    def get(self, request, product_id) :
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)