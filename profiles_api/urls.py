from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#include is used for including lists to assign to a specific url

router = DefaultRouter();
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#this is used to retrieve our route in the router, if we need to retrieve the function


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
