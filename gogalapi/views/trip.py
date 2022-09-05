"""View module for handling requests about trips"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import Trip
from gogalapi.models import GoGalUser

class TripView(ViewSet):
    """Go Gal trip view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE trip
        
        Returns:
            Response -- JSON serialized trip
        """
        try:
            trip = Trip.objects.get(pk=pk)
            serializer = TripSerializer(trip)
            return Response(serializer.data)
        except Trip.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """Handle GET requests to get ALL trips
        
        Returns:
            Response -- JSON serialized list of trips
        """
        trips = Trip.objects.all().order_by("title")
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations for new trip

        Returns
            Response -- JSON serialized trip instance
        """
        user = GoGalUser.objects.get(user=request.auth.user)
        serializer = CreateTripSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
          
class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips"""
    class Meta:
        model = Trip
        fields = ["id", "title", "image_url_one", "image_url_two", "image_url_three", "country", "city", "from_date", "to_date", "content", "user_id"]
        depth = 1
        
        # Why can't I see nested data with the added use of depth? Shouldn't I see the details on the user?
        
class CreateTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["id", "title", "image_url_one", "image_url_two", "image_url_three", "country", "city", "from_date", "to_date", "content", "user_id"]   
        