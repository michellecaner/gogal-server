"""View module for handling requests about My Go Gals"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import MyGoGal

class MyGoGalView(ViewSet):
    """My Go Gal view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE My Go Gal
        
        Returns:
            Response -- JSON serialized My Go Gal
        """
        try:
            my_go_gal = MyGoGal.objects.get(pk=pk)
            serializer = MyGoGalSerializer(my_go_gal)
            return Response(serializer.data)
        except MyGoGal.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def list(self, request):
        """Handle GET requests to get ALL My Go Gals
        
        Returns:
            Response -- JSON serialized list of categories
        """
        my_go_gals = MyGoGal.objects.all()
        serializer = MyGoGalSerializer(my_go_gals, many=True)
        return Response(serializer.data)
      
class MyGoGalSerializer(serializers.ModelSerializer):
    """JSON serializer for My Go Gals"""
    class Meta:
        model = MyGoGal
        fields = ("id", "go_gal_pick", "go_gal_picker")