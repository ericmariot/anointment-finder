from django.db import models


class AnointmentManager(models.Manager):
    # self = Anointment.objects
    # Anointment.objects.with_oil(oil_name="Golden Oil") & (AND) Anointment.objects.with_oil(oil_name="Violet Oil")

    def with_oils(self, *, oil_names: list[str]):
        if len(oil_names) == 0:
            raise ValueError("Anointments uses at least one oil!")

        if len(oil_names) > 3:
            raise ValueError("Anointments can have only up to 3 oils!")

        queryset = self.all()

        for oil_name in oil_names:
            queryset &= (
                self.filter(oil_1__name=oil_name)
                | self.filter(oil_2__name=oil_name)
                | self.filter(oil_3__name=oil_name)
            )

        return queryset
