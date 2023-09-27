import factory
import factory.fuzzy

from anointments.models import Anointment
from oils.models import Oil


class OilFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyChoice(
        ["Golden Oil", "Silver Oil", "Crimson Oil", "Violet Oil"]
    )
    img_link = factory.Faker("file_name", category="image")

    class Meta:
        model = Oil


class AnointmentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("first_name")
    img_link = factory.Faker("file_name", category="image")
    description = factory.Faker("first_name")
    oil_1 = factory.SubFactory(OilFactory)
    oil_2 = factory.SubFactory(OilFactory)
    oil_3 = factory.SubFactory(OilFactory)

    class Meta:
        model = Anointment
