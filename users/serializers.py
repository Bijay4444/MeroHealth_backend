from rest_framework import serializers
from .models import CustomUser, NotificationPreference, CaregiverRelationship

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'age', 'gender', 'is_active', 'is_staff']
        extra_kwargs = {
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
        }

class NotificationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationPreference
        fields = ['id', 'user', 'notification_type', 'is_enabled']

class CaregiverRelationshipSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    caregiver_email = serializers.EmailField(source='caregiver.email', read_only=True)

    class Meta:
        model = CaregiverRelationship
        fields = ['id', 'user', 'caregiver', 'user_email', 'caregiver_email', 'relationship']

