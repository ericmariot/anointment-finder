import json

from anointments.models import Anointment
from oils.models import Oil
from django.core.management.base import BaseCommand

# abs_path = "/Users/ericmariot/projects/annointment-finder/data/all_anointments.json"


class Command(BaseCommand):
    help = "Create anointments from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]

        with open(file_path) as file:
            anointments = json.load(file)

        oils_dict = {oil.name: oil for oil in Oil.objects.all()}

        for anoint in anointments:
            print("\n")
            print("New set of anointments!!")
            oil_names = []
            oils = anoint["oils"]
            outcome = anoint["outcome"]
            anoint_name = outcome["name"]
            anoint_img_link = outcome.get("img_link", "")

            description = "\n".join(outcome["description"])

            print("New set of oils!!")
            for oil_data in oils:
                oil_names.append(oil_data["name"])

            Anointment.objects.update_or_create(
                name=anoint_name,
                defaults=dict(
                    img_link=anoint_img_link,
                    description=description,
                    oil_1=oils_dict[oil_names[0]],
                    oil_2=oils_dict[oil_names[1]],
                    oil_3=oils_dict[oil_names[2]],
                ),
            )
