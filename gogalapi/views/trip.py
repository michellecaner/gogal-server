"""View module for handling requests about trips"""

from logging import raiseExceptions
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import Trip
from gogalapi.models import GoGalUser
from gogalapi.models.category import Category

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
        categories = request.data.get("categories")
        if categories: 
            del request.data["categories"]
        serializer = CreateTripSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        trip = Trip.objects.get(pk=serializer.data["id"])
        if categories:
            for id in categories:
                category = Category.objects.get(pk=id)
                trip.categories.add(category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Handle PUT requests for a trip

        Returns:
            Response -- Empty body with 204 status code
        """
        trip = Trip.objects.get(pk=pk)
        serializer = CreateTripSerializer(trip, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class TripSerializer(serializers.ModelSerializer):
    """JSON serializer for trips"""
    class Meta:
        model = Trip
        fields = ["id", "title", "image_url_one", "image_url_two", "image_url_three", "country", "city", "from_date", "to_date", "content", "user"]
        depth = 2
        
class CreateTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["id", "title", "image_url_one", "image_url_two", "image_url_three", "country", "city", "from_date", "to_date", "content"]   
        