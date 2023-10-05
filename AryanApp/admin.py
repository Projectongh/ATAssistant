from django.contrib import admin

from .models import *
# Register your models here.
class homeAdmin(admin.ModelAdmin):
    list_display = ("productName","price","productImage")
admin.site.register(home,homeAdmin)

# class freeCardAdmin(admin.ModelAdmin):
#     list_display = ("id", "freeicon", "freetitle", "freelink")
#     list_per_page = 4
#     search_fields = ('freetitle',)
#     list_editable = ('freetitle','freelink',)
#     list_filter = ('freetitle',)
# admin.site.register(freeCard,freeCardAdmin)