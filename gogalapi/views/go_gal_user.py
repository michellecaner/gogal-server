"""View module for handling requests about Go Gal users"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from gogalapi.models import GoGalUser

class GoGalUserView(ViewSet):
    """Go Gal user view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for SINGLE Go Gal user
        
        Returns:
            Response -- JSON serialized Go Gal user
        """
        try:
            go_gal_user = GoGalUser.objects.get(pk=pk)
            serializer = GoGalUserSerializer(go_gal_user)
            return Response(serializer.data)
        except GoGalUser.DoesNotExist as ex:
            return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
          
    def list(self, request):
        """Handle GET requests to get ALL Go Gal users
        
        Returns:
            Response -- JSON serialized list of Go Gal users
        """
        go_gal_users = GoGalUser.objects.all()
        serializer = GoGalUserSerializer(go_gal_users, many=True)
        return Response(serializer.data)
      
class GoGalUserSerializer(serializers.ModelSerializer):
    """JSON serializer for Go Gal users"""
    class Meta:
        model = GoGalUser
        fields = ("id", "bio", "profile_img_url", "created_on")
        depth = 1
        
        # What if I wanted to show their name & email from the User model? Or would I take care of that on the front end? This feels related to my question on my trip serializer too.