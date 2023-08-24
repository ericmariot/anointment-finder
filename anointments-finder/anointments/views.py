from django.views.generic import ListView
from .models import Anointment


class AnointmentListView(ListView):
    model = Anointment
    context_object_name = "anointment_list"
    template_name = "anointments/anointment_list.html"
