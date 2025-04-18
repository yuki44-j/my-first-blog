from django.urls import path, include
from django.contrib import admin

from django.contrib.auth import views

from blog.admin import admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path("myadmin/", admin_site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('', include('blog.urls')),
]