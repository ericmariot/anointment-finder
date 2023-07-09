import pytest

from anointments.tests.factories import OilFactory, AnointmentFactory


@pytest.fixture
def all_oils():
    oils = []
    oils.append(OilFactory(name="Golden Oil"))
    oils.append(OilFactory(name="Silver Oil"))
    oils.append(OilFactory(name="Opalescent Oil"))
    oils.append(OilFactory(name="Black Oil"))
    oils.append(OilFactory(name="Crimson Oil"))
    oils.append(OilFactory(name="Violet Oil"))
    oils.append(OilFactory(name="Indigo Oil"))
    oils.append(OilFactory(name="Azure Oil"))
    oils.append(OilFactory(name="Teal Oil"))
    oils.append(OilFactory(name="Verdant Oil"))
    oils.append(OilFactory(name="Amber Oil"))
    oils.append(OilFactory(name="Sepia Oil"))
    oils.append(OilFactory(name="Clear Oil"))

    return oils


@pytest.fixture
def golden_anointments(all_oils):
    anointments = []
    anointments.append(AnointmentFactory(oil_1=all_oils[0]))
    anointments.append(AnointmentFactory(oil_1=all_oils[0], oil_2=all_oils[0]))
    anointments.append(AnointmentFactory(oil_1=all_oils[0], oil_3=all_oils[0]))
    anointments.append(AnointmentFactory(oil_2=all_oils[0], oil_3=all_oils[0]))
    anointments.append(
        AnointmentFactory(oil_1=all_oils[0], oil_2=all_oils[0], oil_3=all_oils[0])
    )
    return anointments


@pytest.fixture
def silver_or_opalescent_anointments(all_oils):
    anointments = []
    # Silver
    anointments.append(AnointmentFactory(oil_1=all_oils[1]))
    anointments.append(AnointmentFactory(oil_1=all_oils[1], oil_2=all_oils[1]))
    anointments.append(AnointmentFactory(oil_1=all_oils[1], oil_3=all_oils[1]))
    anointments.append(AnointmentFactory(oil_2=all_oils[1], oil_3=all_oils[1]))
    anointments.append(
        AnointmentFactory(oil_1=all_oils[1], oil_2=all_oils[1], oil_3=all_oils[1])
    )

    # Opalescent
    anointments.append(AnointmentFactory(oil_1=all_oils[2]))
    anointments.append(AnointmentFactory(oil_1=all_oils[2], oil_2=all_oils[2]))
    anointments.append(AnointmentFactory(oil_1=all_oils[2], oil_3=all_oils[2]))
    anointments.append(AnointmentFactory(oil_2=all_oils[2], oil_3=all_oils[2]))
    anointments.append(
        AnointmentFactory(oil_1=all_oils[2], oil_2=all_oils[2], oil_3=all_oils[2])
    )
    return anointments


@pytest.fixture
def many_anointments(all_oils):
    anointments = []
    anointments.append(
        AnointmentFactory(oil_1=all_oils[3], oil_2=all_oils[4], oil_3=all_oils[5])
    )
    anointments.append(
        AnointmentFactory(oil_1=all_oils[4], oil_2=all_oils[4], oil_3=all_oils[4])
    )
    anointments.append(
        AnointmentFactory(oil_1=all_oils[5], oil_2=all_oils[4], oil_3=all_oils[3])
    )
    anointments.append(
        AnointmentFactory(oil_1=all_oils[6], oil_2=all_oils[7], oil_3=all_oils[8])
    )
    anointments.append(
        AnointmentFactory(oil_1=all_oils[7], oil_2=all_oils[7], oil_3=all_oils[7])
    )
    anointments.append(
        AnointmentFactory(oil_1=all_oils[8], oil_2=all_oils[7], oil_3=all_oils[6])
    )
    return anointments
