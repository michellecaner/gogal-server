"""View module for handling requests about trip categories"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import TripCategory

class TripCategoryView(ViewSet):
    """Go Gal trip category view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE trip category
        
        Returns:
            Response -- JSON serialized trip category
        """
        try:
            trip_category = TripCategory.objects.get(pk=pk)
            serializer = TripCategorySerializer(trip_category)
            return Response(serializer.data)
        except TripCategory.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL trip categories
        
        Returns:
            Response -- JSON serialized list of trip categories
        """
        trip_categories = TripCategory.objects.all()
        serializer = TripCategorySerializer(trip_categories, many=True)
        return Response(serializer.data)
      
class TripCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for trip categories"""
    class Meta:
        model = TripCategory
        fields = ["id", "category_id", "trip_id"]
        depth = 2