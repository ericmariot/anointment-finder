import json

from oils.models import Oil
from django.core.management.base import BaseCommand, CommandError, no_translations

abs_path = "/Users/ericmariot/projects/annointment-finder/data/all_oils.json"

class Command(BaseCommand):
    help = "Create oils from a JSON file"

    def handle(self, *args, **options):
        with open(abs_path) as file:
            oils = json.load(file)
        
        for oil in oils:
            o = Oil(name=oil['name'], img_link=['img_link'])
            o.save()