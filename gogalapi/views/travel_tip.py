"""View module for handling requests about travel tips"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import TravelTip

class TravelTipView(ViewSet):
    """Go Gal travel tip view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE travel tip
        
        Returns:
            Response -- JSON serialized travel tip
        """
        try:
            travel_tip = TravelTip.objects.get(pk=pk)
            serializer = TravelTipSerializer(travel_tip)
            return Response(serializer.data)
        except TravelTip.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def list(self, request):
        """Handle GET requests to get ALL travel tips
        
        Returns:
            Response -- JSON serialized list of travel tips
        """
        travel_tips = TravelTip.objects.all()
        serializer = TravelTipSerializer(travel_tips, many=True)
        return Response(serializer.data)
      
class TravelTipSerializer(serializers.ModelSerializer):
    """JSON serializer for travel tips"""
    class Meta:
        model = TravelTip
        fields = ["id", "tip"]
