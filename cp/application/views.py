from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import CustomerDetails
from .models import TRX_CENTRAL
from .models import INV_DB
from .models import ASSETS
from django.shortcuts import render

from rest_framework import viewsets

from .serializers import CustomerDetailsSerializer
from .serializers import TRX_CENTRALSerializer
from .serializers import INV_DBSerializer
from .serializers import ASSETSSerializer


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class CustomerDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerDetailsSerializer
    queryset = CustomerDetails.objects.all()

class TRX_CENTRALViewSet(viewsets.ModelViewSet):
    serializer_class = TRX_CENTRALSerializer
    queryset = TRX_CENTRAL.objects.all()

class INV_DBViewSet(viewsets.ModelViewSet):
    serializer_class = INV_DBSerializer
    queryset = INV_DB.objects.all()

class ASSETSViewSet(viewsets.ModelViewSet):
    serializer_class = ASSETSSerializer
    queryset = ASSETS.objects.all()


