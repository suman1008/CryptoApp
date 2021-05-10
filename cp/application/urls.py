from django.contrib import admin
from django.urls import path, include
from .import views

from rest_framework import routers

from .views import CustomerDetailsViewSet
from .views import TRX_CENTRALViewSet
from .views import INV_DBViewSet
from .views import ASSETSViewSet


router = routers.DefaultRouter()

router.register('KYC', CustomerDetailsViewSet)
router.register('AllTransactions', TRX_CENTRALViewSet)
router.register('InvestmentsDB', INV_DBViewSet)
router.register('ASSETS', ASSETSViewSet)



urlpatterns = [
    path('', include(router.urls)),

]