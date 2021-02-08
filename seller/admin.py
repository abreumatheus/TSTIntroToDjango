from django.contrib import admin

from seller.models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')


admin.site.register(Seller, SellerAdmin)
