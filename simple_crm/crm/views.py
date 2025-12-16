from rest_framework.generics import ListAPIView
from .models import Client, Deal
from .serializers import ClientSerializer, DealSerializer


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DealListAPIView(ListAPIView):
    serializer_class = DealSerializer

    def get_queryset(self):
        queryset = Deal.objects.select_related("client")
        status = self.request.query_params.get("status")

        if status:
            queryset = queryset.filter(status=status)

        return queryset
