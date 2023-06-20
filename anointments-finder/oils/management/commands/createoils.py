import json

from oils.models import Oil
from django.core.management.base import BaseCommand

# abs_path = "/Users/ericmariot/projects/annointment-finder/data/all_oils.json"


class Command(BaseCommand):
    help = "Create oils from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]

        with open(file_path) as file:
            oils = json.load(file)

        for oil in oils:
            Oil.objects.update_or_create(
                name=oil["name"],
                defaults={"img_link": oil["img_link"]},
            )
