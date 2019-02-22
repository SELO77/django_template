from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy


class RCAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_header = gettext_lazy('Admin')
    # Text to put in each page's <h1>.
    site_title = gettext_lazy('Admin')
    # Text to put at the top of the admin index page.
    index_title = gettext_lazy('Admin')


admin_site = RCAdminSite()