# from django.contrib.admin import AdminSite
# from django.utils.translation import gettext_lazy
#
#
# class DTAdminSiteBase(AdminSite):
#     # Text to put at the end of each page's <title>.
#     site_header = gettext_lazy('Admin')
#     # Text to put in each page's <h1>.
#     site_title = gettext_lazy('Admin')
#     # Text to put at the top of the admin index page.
#     index_title = gettext_lazy('Admin')
#
#     # URL for the "View site" link at the top of each admin page.
#     # site_url = '/'
#     #
#     # _empty_value_display = '-'
#     #
#     # login_form = None
#     # index_template = None
#     # app_index_template = None
#     # login_template = None
#     # logout_template = None
#     # password_change_template = None
#     # password_change_done_template = None
#
#
# class DTAdminSite(DTAdminSiteBase):
#     pass
#
#
# admin_site = DTAdminSite
from django.contrib import admin

admin.site.site_header = 'Admin'
admin.site.site_title = 'Admin'

admin_urls = admin.site.urls