#
# # Register your models here.
# from django.contrib import admin
#
# from core.account.models import DTUser
# from core.admin import admin_site, DTAdminSite
#
#
# # @admin_site.register(DTUser)
# # # class DTUserAdmin(admin.ModelAdmin):
# # #     pass
from django.contrib import admin

from core.account.models import DTUser


@admin.register(DTUser)
class DTUserAdmin(admin.ModelAdmin):
    pass
