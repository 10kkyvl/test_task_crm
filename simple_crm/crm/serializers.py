from rest_framework import serializers
from .models import Client, Deal


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "name", "phone", "email", "created_at")


class DealSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()

    class Meta:
        model = Deal
        fields = (
            "id",
            "title",
            "client",
            "amount",
            "status",
            "created_at",
        )

    def get_client(self, obj):
        return {
            "id": obj.client_id,
            "name": obj.client.name,
        }
