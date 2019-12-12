from rest_framework import serializers

from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile #set our serializer to point to user profile model
        fields = ('id', 'email', 'name', 'password') #fields needed to create new users
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        #to guard our password from being read

    def create(self, validated_data):
        #this function overrides the create_user function
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed item """
    class Meta:
        model = models.ProfileFeedItem #set our serializer to point to profile feed ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on') #always include id so you can search
        #id is automatically created, so it is readonly
        #only fields writable is status_text, user_profile must be of the user own making it readonly
        extra_kwargs = {
            'user_profile': {
                'read_only': True,

            }
        }
