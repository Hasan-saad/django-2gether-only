from .models import ServicProvider
from .serializers import ServiceProviderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def service_provider_api(request):
        apiList = ServicProvider.objects.all()
        jsonList = ServiceProviderSerializer(apiList, many=True).data
        return Response({'jsonList': jsonList})

@api_view(['GET'])
def service_provider_api_id(request, id):
        apiList = ServicProvider.objects.get(id=id)
        jsonList = ServiceProviderSerializer(apiList).data
        return Response({'jsonList': jsonList})


class ServiceProviderDetail(generics.ListCreateAPIView):
    queryset = ServicProvider.objects.all()
    serializer_class = ServiceProviderSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = ServicProvider.objects.all()
        serializer_class = ServiceProviderSerializer
        lookup_field = 'id'