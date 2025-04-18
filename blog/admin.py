from django.contrib import admin
from .models import Post

class MyAdminSite(admin.AdminSite):
    site_header = "Blog administration"

admin_site = MyAdminSite(name="myadmin")
admin.site.register(Post)