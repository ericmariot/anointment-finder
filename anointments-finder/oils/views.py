from django.views.generic import ListView
from .models import Oil


class OilListView(ListView):
    model = Oil
    context_object_name = "oil_list"
    template_name = "oils/oil_list.html"
