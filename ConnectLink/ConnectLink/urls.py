from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("user_app.urls")),
    path("api/", include("connect_link.urls"))
]
