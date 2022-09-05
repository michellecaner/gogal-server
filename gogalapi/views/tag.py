"""View module for handling requests about tags"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import Tag

class TagView(ViewSet):
    """Go Gal tag view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE tag
        
        Returns:
            Response -- JSON serialized tag
        """
        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag)
            return Response(serializer.data)
        except Tag.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
    def list(self, request):
        """Handle GET requests to get ALL tags
        
        Returns:
            Response -- JSON serialized list of tags
        """
        tags = Tag.objects.all().order_by('label')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
      
class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for categories"""
    class Meta:
        model = Tag
        fields = ("id", "label")
