from django.contrib import admin
from .models import KeyToken, HostDomain
# Register your models here.
class KeyTokenAdmin(admin.ModelAdmin):
    readonly_fields =('access_token',)
admin.site.register(KeyToken, KeyTokenAdmin)
admin.site.register(HostDomain)
