from django.db import models

# Create your models here.
class Currency(models.Model):
    name = models.CharField(unique=True, max_length=20, blank=False, null=False);
    symbol = models.CharField(max_length=8, blank=False, null=False);

    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name;