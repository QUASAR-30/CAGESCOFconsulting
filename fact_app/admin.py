from django.contrib import admin
from .models import * 
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'sex', 'age', 'city', 'zip_code')

class AdminInvoice(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'invoice_date_time', 'total', 'last_updated_date', 'paid', 'invoice_type')

admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)

class AdminDocument(admin.ModelAdmin):
    list_display = ('customer', 'save_by', 'document_type', 'creation_date', 'last_updated_date')
    search_fields = ('customer__name', 'save_by__username', 'document_type')
    list_filter = ('document_type', 'creation_date')
    date_hierarchy = 'creation_date'

admin.site.register(Document, AdminDocument)


admin.site.site_title = _("CAGESCOF Consulting SYSTEM")
admin.site.site_header = _("CAGESCOF Consulting SYSTEM")
admin.site.index_title = _("CAGESCOF Consulting SYSTEM")