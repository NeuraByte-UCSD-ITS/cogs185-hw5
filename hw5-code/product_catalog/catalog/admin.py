from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'quantity', 'expiry_date', 'created_at')
    search_fields = ('name', 'serial_number')
