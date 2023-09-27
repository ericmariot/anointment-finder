from django.views.generic import TemplateView
from anointments.models import Anointment
from anointments.script_filter import find_anointments
from oils.models import Oil


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["oils"] = Oil.objects.all()

        # self.request.GET
        # <QueryDict: {'oil': ['31']}>
        # with the value inside the dict, call the functions to filter anointments
        if oils := self.request.GET.getlist("oil"):
            context["anointments"] = find_anointments(set(oils))
        else:
            context["anointments"] = Anointment.objects.all()

        return context
