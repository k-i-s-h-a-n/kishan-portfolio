from django.contrib import admin
from kishan.models import contact

# Register your models here.




class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ['name', 'email', 'subject', 'message']

admin.site.register(contact, ContactAdmin)