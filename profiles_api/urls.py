from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#include is used for including lists to assign to a specific url

router = DefaultRouter();
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#this is used to retrieve our route in the router, if we need to retrieve the function
router.register('profile', views.UserProfileViewSet)
#dont need to provide base_name because in UserProfileViewSet queryset has been defined
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
