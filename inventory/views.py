from rest_framework.views import APIView
from rest_framework.response import Response


class InventoryList(APIView):

    def get(self, request, format=None):
        return Response({1: 'test'})


    # def delete(self, request, format=None):
