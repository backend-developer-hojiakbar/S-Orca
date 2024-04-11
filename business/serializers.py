from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        if not validated_data.get('terms_of_service'):
            raise serializers.ValidationError("You must agree to the terms of service.")

        return super().create(validated_data)
