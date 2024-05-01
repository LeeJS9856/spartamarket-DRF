from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductAPIView.as_view(), name="productAPIView"),
    path("<int:product_id>/", views.ProductDetailAPIView.as_view()),
    path("<int:product_id>/like/", views.ProductLikeAPIView.as_view()),
]