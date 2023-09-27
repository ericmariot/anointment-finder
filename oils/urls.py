from django.urls import path

from .views import OilListView

urlpatterns = [
    path("", OilListView.as_view(), name="oil_list"),
]
