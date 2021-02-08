from django.db import models


class Seller(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
