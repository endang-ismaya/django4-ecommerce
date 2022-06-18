from django.contrib import admin
from .models import Product

# Register your models here.

# modify admin panel
admin.site.site_header = "Buy & Sell Website"
admin.site.site_title = "ABC Buying"
admin.site.index_title = "Manage ABC Buying Website"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "desc", "seller_name")
    search_fields = ("name",)
    actions = ("set_price_to_zero",)
    list_editable = ("price", "desc")

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)
