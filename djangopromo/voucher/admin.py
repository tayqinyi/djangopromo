from django.contrib import admin
from .models import FixedVoucher, PercentVoucher


# Register your models here.
class VoucherAdmin(admin.ModelAdmin):
    list_display = ('code', 'amount', 'uses')


admin.site.register([FixedVoucher,
                     PercentVoucher], VoucherAdmin)