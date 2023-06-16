import json

from anointments.models import Anointment
from oils.models import Oil
from django.core.management.base import BaseCommand

abs_path = "/Users/ericmariot/projects/annointment-finder/data/all_anointments.json"


class Command(BaseCommand):
    help = "Create anointments from a JSON file"

    def handle(self, *args, **options):
        with open(abs_path) as file:
            anointments = json.load(file)

        for anoint in anointments:
            print("\n")
            print("New set of anointments!!")
            oil_names = []
            oils = anoint["oils"]
            outcome = anoint["outcome"]
            anoint_name = outcome["name"]
            anoint_img_link = outcome["img_link"]
            description = "\n".join(outcome["description"])

            print("New set of oils!!")
            for oil_data in oils:
                oil_names.append(oil_data["name"])


            _obj, _created = Anointment.objects.get_or_create(
                name=anoint_name,
                img_link=anoint_img_link,
                description=description,
                oil_1=Oil.objects.get(name=oil_names[0]),
                oil_2=Oil.objects.get(name=oil_names[1]),
                oil_3=Oil.objects.get(name=oil_names[2]),
            )
