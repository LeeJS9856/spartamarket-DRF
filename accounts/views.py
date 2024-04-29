from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import AccountSerializer, AccountDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import User


class AccountAPIView(APIView):
    def post(self, request):
        user_data = AccountSerializer(data = request.data)
        if user_data.is_valid(raise_exception=True):
            user_data.save()
            return Response(user_data.data, status=status.HTTP_201_CREATED)
        

class AccountDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, username):
        return get_object_or_404(get_user_model(), username = username)

    def get(self, request, username):
        if username == request.user.username:
            serializer = AccountDetailSerializer(self.get_object(username))
            return Response(serializer.data)
