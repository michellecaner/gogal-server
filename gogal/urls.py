"""gogal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from gogalapi.views import register_user, login_user
from gogalapi.views import CategoryView
from gogalapi.views import GoGalUserView
from gogalapi.views import MyGoGalView
from gogalapi.views import TagView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryView, "category")
router.register(r'go_gal_users', GoGalUserView, "go_gal_user")
router.register(r'my_go_gals', MyGoGalView, "my_go_gal")
router.register(r'tags', TagView, "tag")

urlpatterns = [
    path("register", register_user),
    path("login", login_user),
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
