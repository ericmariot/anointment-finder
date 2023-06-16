import json

from oils.models import Oil
from django.core.management.base import BaseCommand

abs_path = "/Users/ericmariot/projects/annointment-finder/data/all_oils.json"


class Command(BaseCommand):
    help = "Create oils from a JSON file"

    def handle(self, *args, **options):
        with open(abs_path) as file:
            oils = json.load(file)

        for oil in oils:
            _obj, _created = Oil.objects.get_or_create(
                name=oil["name"],
                img_link=["img_link"]
            )
