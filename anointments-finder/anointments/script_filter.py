from anointments.models import Anointment
from itertools import product


def find_anointments(oil_names: list[str]):
    if len(oil_names) == 1:
        return Anointment.objects.with_oils(oil_names=[oil_names[0]])

    if len(oil_names) == 2:
        return Anointment.objects.with_oils(
            oil_names=[oil_names[0]]
        ) | Anointment.objects.with_oils(oil_names=[oil_names[1]])

    queryset = Anointment.objects.none()

    for oil_name in product(oil_names, repeat=3):
        queryset |= (
            Anointment.objects.filter(oil_1__name=oil_name)
            & Anointment.objects.filter(oil_2__name=oil_name)
            & Anointment.objects.filter(oil_3__name=oil_name)
        )

    return queryset
