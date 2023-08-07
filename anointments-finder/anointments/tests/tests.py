import pytest

from anointments.script_filter import find_anointments
from anointments.tests.factories import AnointmentFactory


@pytest.mark.django_db
class TestFindAnointments:
    def test_with_one_oil_find_all_that_use_golden(self):
        golden = AnointmentFactory(oil_1__name="Golden Oil")
        AnointmentFactory(
            oil_1__name="Silver Oil", oil_2__name="Silver Oil", oil_3__name="Silver Oil"
        )

        find_all = find_anointments({"Golden Oil"})

        assert find_all == [golden]

    def test_with_one_oil_find_all_that_use_silver_or_opalescent(self):
        silver = AnointmentFactory(oil_1__name="Silver Oil")
        opalescent = AnointmentFactory(oil_1__name="Opalescent Oil")
        AnointmentFactory(
            oil_1__name="Crimson Oil",
            oil_2__name="Crimson Oil",
            oil_3__name="Crimson Oil",
        )
        find_all = find_anointments({"Silver Oil", "Opalescent Oil"})

        assert silver in find_all
        assert opalescent in find_all
        assert len(find_all) == 2

    def test_oil_combinations(self):
        anointments = {
            AnointmentFactory(
                oil_1__name="Black Oil",
                oil_2__name="Crimson Oil",
                oil_3__name="Violet Oil",
            ),
            AnointmentFactory(
                oil_1__name="Teal Oil",
                oil_2__name="Azure Oil",
                oil_3__name="Indigo Oil",
            ),
        }
        AnointmentFactory(
            oil_1__name="Opalescent Oil",
            oil_2__name="Silver Oil",
            oil_3__name="Opalescent Oil",
        )
        find_all = find_anointments(
            {
                "Black Oil",
                "Crimson Oil",
                "Violet Oil",
                "Indigo Oil",
                "Azure Oil",
                "Teal Oil",
            }
        )

        assert set(find_all) == anointments
