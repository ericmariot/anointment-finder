from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("pages.urls")),
    path("oils/", include("oils.urls")),
    path("admin/", admin.site.urls),
]
