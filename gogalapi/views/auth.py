from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from gogalapi.models import GoGalUser

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    """Handles the authentication of a Go Gal user
    
    Method arguments:
      request -- The full HTTP request object
    """
    username = request.data["username"]
    password = request.data["password"]
    
    authenticated_user = authenticate(username=username, password=password)
    
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            "valid": True,
            "token": token.key
        }
        return Response(data)
    else:
        data = { "valid": False }
        return Response(data)

@api_view(["POST"])
@permission_classes([AllowAny])
def register_user(request):
    """Handles the creation of a new Go Gal user for authentication

    Method Arguments:
        request -- The full HTTP request object
    """
    
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name']
    )
    
    go_gal_user = GoGalUser.objects.create(
          bio=request.data["bio"],
          profile_img_url=request.data["profile_img_url"],
        #   created_on=request.data["created_on"],
        #   active=request.data["active"],
          user=new_user
    )
    
    token = Token.objects.create(user=go_gal_user.user)
    data = { "token": token.key }
    return Response(data, status=status.HTTP_201_CREATED)