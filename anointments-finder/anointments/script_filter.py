from anointments.models import Anointment


def find_anointments(oil_names: set[str]):
    anointments = Anointment.objects.all()
    result = []

    if len(oil_names) <= 2:
        for anointment in anointments:
            oil_set = {oil.name for oil in anointment.oils}

            if oil_names.intersection(oil_set):
                result.append(anointment)
    else:
        for anointment in anointments:
            oil_set = {oil.name for oil in anointment.oils}

            if oil_set.issubset(oil_names):
                result.append(anointment)

    return result
