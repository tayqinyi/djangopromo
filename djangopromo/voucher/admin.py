from django.contrib import admin
from .models import FixedVoucher, PercentVoucher

# Register your models here.
admin.site.register([FixedVoucher,
                     PercentVoucher])