from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

class AccountAPIView(APIView):
    def post(self, request):
        user_data = AccountSerializer(data = request.data)
        if user_data.is_valid(raise_exception=True):
            user_data.save()
            return Response(user_data.data, status=status.HTTP_201_CREATED)
# Create your views here.
