from django.contrib import admin
from logs.models import Log
# Register your models here.

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('card_scanned', 'member_name', 'scanned_at', 'status_at_scan')
    readonly_fields = ('card_scanned', 'member_name', 'scanned_at', 'status_at_scan')
    can_delete = False
    list_per_page = 10
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False