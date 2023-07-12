from anointments.models import Anointment


def find_anointments(oil_names: set[str]):
    # SELECT * FROM anointments_anointment
    # SELECT * FROM anointments_anointment JOIN oils_oil ON anointments_anointment.oil_1_id = oils_oil.id JOIN oils_oil...;
    anointments = Anointment.objects.select_related("oil_1", "oil_2", "oil_3").all()
    condition = "intersection" if len(oil_names) <= 2 else "issubset"
    result = []

    for anointment in anointments:
        oil_set = {oil.name for oil in anointment.oils}

        if getattr(oil_set, condition)(oil_names):
            result.append(anointment)

    return result
