from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from core.models import Currency


# Create your models here.
class BaseVoucher(models.Model):
    code = models.CharField(unique=True, max_length=8, blank=False, null=False);
    amount = models.DecimalField(default=10, max_digits=10, decimal_places=2, blank=False, null=False)
    uses = models.IntegerField(default=3, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.code

    def clean(self):
        if len(self.code) < 5 or len(self.code) > 8:
            raise ValidationError({'code': 'The code length should be 5-8 characters.'})
        elif self.amount <= 0:
            raise ValidationError({'amount': 'Amount should be larger than 0.'})

    def get_absolute_url(self):
        return reverse('voucher')

class FixedVoucher(BaseVoucher):

    class Meta:
        verbose_name = 'fixed voucher'
        verbose_name_plural = 'fixed vouchers'

    currency = models.OneToOneField(Currency, on_delete=models.DO_NOTHING)


class PercentVoucher(BaseVoucher):

    class Meta:
        verbose_name = 'percent voucher'
        verbose_name_plural = 'percent vouchers'

    def clean(self):
        super().clean()
        if self.amount >= 100:
            raise ValidationError({'amount': 'Percent discount should be less than 100.'})
