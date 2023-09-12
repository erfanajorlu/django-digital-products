from django.contrib import admin
from .models import Gateway, Payment

@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'get_gateway_title', 'price', 'status', 'phone_number', 'created_time']
    list_filter = ['status', 'gateway']  # Filter by the foreign key field
    search_fields = ['user__username', 'phone_number']

    def get_gateway_title(self, obj):
        return obj.gateway.title

    get_gateway_title.admin_order_field = 'gateway__title'
    get_gateway_title.short_description = 'Gateway Title'