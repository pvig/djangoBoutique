from boutique.models import Vente
from boutique.models import Produit
from boutique.models import Client
from boutique.serializers import VenteSerializer
from boutique.serializers import ProduitSerializer
from boutique.serializers import ClientSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#For yasg
from drf_yasg.utils import swagger_auto_schema

class VenteList(APIView):
    '''
    List all ventes or create a new vente
    '''
    @swagger_auto_schema(
        responses={200: VenteSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No ventes found'},
        tags=['Get Ventes'],
        operation_description="Method to fetch all the ventes",
    )
    def get(self,request,format=None):
        print("Get ventes list called")
        ventes = Vente.objects.all()
        serializer = VenteSerializer(ventes, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to post a new vente",
        request_body=VenteSerializer,
        responses={200: VenteSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Vente Added'},
        tags=['Create, Update and Delete Vente'],
        operation_description="Method to post a new Vente",
    )
    def post(self, request, format=None):
        print("Create vente called")
        serializer = VenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VenteDetail(APIView):
    """
    Retrieve, update or delete a vente instance.
    """
    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Vente.objects.get(pk=pk)
        except Vente.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: VenteSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No vente found for the given id'},
        tags=['Get Ventes'],
        operation_description="Method to fetch a vente",
    )
    def get(self, request, pk, format=None):
        vente = self.get_object(pk)
        serializer = VenteSerializer(vente)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to update a vente",
        request_body=VenteSerializer,
        responses={200: VenteSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Vente updated'},
        tags=['Create, Update and Delete Vente'],
        operation_description="Method to update a vente",
    )
    def put(self, request, pk, format=None):
        vente = self.get_object(pk)
        serializer = VenteSerializer(vente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        description="Method to delete a vente",
        request_body=VenteSerializer,
        responses={200: VenteSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Vente deleted'},
        tags=['Create, Update and Delete Vente'],
        operation_description="Method to update a vente",
    )    
    def delete(self, request, pk, format=None):
        vente = self.get_object(pk)
        vente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientList(APIView):
    '''
    List all clients or create a new client
    '''
    @swagger_auto_schema(
        responses={200: ClientSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No clients found'},
        tags=['Get Clients'],
        operation_description="Method to fetch all the clients",
    )
    def get(self,request,format=None):
        print("Get clients list called")
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=ClientSerializer,
        responses={200: ClientSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Client Added'},
        tags=['Create, Update and Delete Client'],
        operation_description="Method to post a new Client",
    )
    def post(self, request, format=None):
        print("Create client called")
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    """
    Retrieve, update or delete a client instance.
    """
    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: ClientSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No client found for the given id'},
        tags=['Get Clients'],
        operation_description="Method to fetch a client",
    )
    def get(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to update a client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Client updated'},
        tags=['Create, Update and Delete Client'],
        operation_description="Method to update a client",
    )
    def put(self, request, pk, format=None):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        description="Method to delete a client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Client deleted'},
        tags=['Create, Update and Delete Client'],
        operation_description="Method to update a client",
    )    
    def delete(self, request, pk, format=None):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProduitList(APIView):
    '''
    List all produits or create a new produit
    '''
    @swagger_auto_schema(
        responses={200: ProduitSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No produits found'},
        tags=['Get Produits'],
        operation_description="Method to fetch all the produits",
    )
    def get(self,request,format=None):
        print("Get produits list called")
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to post a new building",
        request_body=ProduitSerializer,
        responses={200: ProduitSerializer(many=False),
                   401: 'Unauthorized',
                   201: 'Produit Added'},
        tags=['Create, Update and Delete Produit'],
        operation_description="Method to post a new Produit",
    )
    def post(self, request, format=None):
        print("Create produit called")
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProduitDetail(APIView):
    """
    Retrieve, update or delete a produit instance.
    """
    @swagger_auto_schema(
        auto_schema=None,
    )
    def get_object(self, pk):
        try:
            return Produit.objects.get(pk=pk)
        except Produit.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        responses={200: ProduitSerializer(many=True),
                   401: 'Unauthorized',
                   404: 'No produit found for the given id'},
        tags=['Get Produits'],
        operation_description="Method to fetch a produit",
    )
    def get(self, request, pk, format=None):
        produit = self.get_object(pk)
        serializer = ProduitSerializer(produit)
        return Response(serializer.data)

    @swagger_auto_schema(
        description="Method to update a produit",
        request_body=ProduitSerializer,
        responses={200: ProduitSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Produit updated'},
        tags=['Create, Update and Delete Produit'],
        operation_description="Method to update a produit",
    )
    def put(self, request, pk, format=None):
        produit = self.get_object(pk)
        serializer = ProduitSerializer(produit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        description="Method to delete a produit",
        request_body=ProduitSerializer,
        responses={200: ProduitSerializer(many=True),
                   401: 'Unauthorized',
                   201: 'Produit deleted'},
        tags=['Create, Update and Delete Produit'],
        operation_description="Method to update a produit",
    )    
    def delete(self, request, pk, format=None):
        produit = self.get_object(pk)
        produit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
