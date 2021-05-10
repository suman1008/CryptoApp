from django.contrib import admin
from .models import CustomerDetails
from .models import TRX_CENTRAL
from .models import INV_DB
from .models import ASSETS

# Register your models here.

admin.site.register(CustomerDetails)
admin.site.register(TRX_CENTRAL)
admin.site.register(INV_DB)
admin.site.register(ASSETS)