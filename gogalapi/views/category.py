"""View module for handling requests about categories"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import Category

class CategoryView(ViewSet):
    """Go Gal category view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE category
        
        Returns:
            Response -- JSON serialized category
        """
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
      
    def list(self, request):
        """Handle GET requests to get ALL categories
        
        Returns:
            Response -- JSON serialized list of categories
        """
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
      
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""
    class Meta:
        model = Category
        fields = ("id", "label")
