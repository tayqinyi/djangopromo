from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import VoucherForm
from .models import BaseVoucher

class VoucherView(FormView):
    template_name = 'home.html'
    form_class = VoucherForm
    success_url = '/'

    def form_valid(self, form):
        voucher = BaseVoucher.objects.filter(code=form.cleaned_data['code']).select_subclasses().first()

        if voucher:
            voucher.uses -= 1
            messages.success(self.request, f'Voucher [{voucher.code}] applied, {voucher.get_discount_display()} discount, {voucher.uses} uses remaining')
            if voucher.uses == 0:
                voucher.delete()
            else:
                voucher.save()
        else:
            messages.error(self.request, 'Voucher code invalid')

        return super().form_valid(form)
