"""View module for handling requests about trip tags"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import TripTag

class TripTagView(ViewSet):
    """Go Gal trip tag view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE trip tag
        
        Returns:
            Response -- JSON serialized trip tag
        """
        try:
            trip_tag = TripTag.objects.get(pk=pk)
            serializer = TripTagSerializer(trip_tag)
            return Response(serializer.data)
        except TripTag.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get ALL trip tags
        
        Returns:
            Response -- JSON serialized list of trip tags
        """
        trip_tags = TripTag.objects.all()
        serializer = TripTagSerializer(trip_tags, many=True)
        return Response(serializer.data)
      
class TripTagSerializer(serializers.ModelSerializer):
    """JSON serializer for trip tags"""
    class Meta:
        model = TripTag
        fields = ("id", "tag_id", "trip_id")
        depth = 2