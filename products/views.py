from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
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
        pagenator = Paginator(products, 30)
        page_number = request.GET.get("page")
        page_product = pagenator.get_page(page_number)
        serializers = ProductSerializer(page_product, many=True)
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

    def get_object(self, product_id):
        return get_object_or_404(Product, pk=product_id)
    
    def get(self, request, product_id) :
        product = self.get_object(product_id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, product_id) :
        product = self.get_object(product_id)
        if product.author == request.user :
            serializer = ProductDetailSerializer(product, data = request.data, partial=True)
            if serializer.is_valid(raise_exception=True) :
                serializer.save()
                return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, product_id):
        product = self.get_object(product_id)
        if product.author == request.user :
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
        
    def dispatch(self, request, product_id):
        if request.method == 'GET':
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated]
        return super().dispatch(request, product_id)