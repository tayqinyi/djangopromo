from django.db import models
from django.core.exceptions import ValidationError
from core.models import Currency

# Create your models here.
class BaseVoucher(models.Model):
    code = models.CharField(unique=True, max_length=8, blank=False, null=False);
    amount = models.DecimalField(default=10, max_digits=10, decimal_places=2, blank=False, null=False)
    uses = models.IntegerField(default=3)

    def __str__(self):
        return self.code

    def clean(self):
        if len(self.code) < 5 or len(self.code) > 8:
            raise ValidationError({'code': 'The code length should be 5-8 characters.'})

class FixedVoucher(BaseVoucher):
    currency = models.OneToOneField(Currency, on_delete=models.DO_NOTHING)

class PercentVoucher(BaseVoucher):

    def clean(self):
        super().clean()
        if self.quantity <=0 or self.quantity >= 100:
            raise ValidationError({'quantity': 'Percent discount should be between 0 to 100.'})


