from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "like_articles")

