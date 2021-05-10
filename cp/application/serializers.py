from rest_framework import serializers
from .models import CustomerDetails
from .models import TRX_CENTRAL
from .models import INV_DB
from .models import ASSETS


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = ['C_ID', 'Customer_Name', 'PAN', 'Adhaar', 'Passport', 'Residential_Address', 'Phone', 'Email', 'Birth_Date']

class TRX_CENTRALSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRX_CENTRAL
        fields = ['TRX_ID', 'customer_ID', 'Name', 'Amount_USD', 'IN_OUT', 'Date_Time_Stamp']

class INV_DBSerializer(serializers.ModelSerializer):
    class Meta:
        model = INV_DB
        fields = ['Asset_Name', 'Qty', 'CP', 'SP']

class ASSETSSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASSETS
        fields = ['Asset_Name']

