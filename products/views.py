from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
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
        cache_key = "product_list"
        products = Product.objects.all()

        categorie = request.GET.get('categorie')
        if categorie == 'title' :
            search = request.GET.get("search")
            products = products.filter(title__contains=search)
        elif categorie == 'nickname' :
            search = request.GET.get("search")
            products = products.filter(author__contians=search)
        elif categorie == 'content' :
            search = request.GET.get("search")
            products = products.filter(content__contians=search)

        pagenator = Paginator(products, 30)
        page_number = request.GET.get("page")
        if page_number is not None :
            products = pagenator.get_page(page_number)

        serializers = ProductSerializer(products, many=True)
        json_data = serializers.data
        cache.set(cache_key, json_data, 180)
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
    
class ProductLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, product_id) :
        product = get_object_or_404(Product, id=product_id)
        if product.like_users.filter(id=request.user.id).exists() :
            product.like_users.remove(request.user)
        else :
            product.like_users.add(request.user)
        return Response(status=status.HTTP_200_OK)
