from rest_framework import serializers
from .models import UserProfile, Club

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'profile_pic', 'date_created', 'is_active', 'is_staff', 'owned_clubs', 'clubs')


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'description', 'owner', 'members')

