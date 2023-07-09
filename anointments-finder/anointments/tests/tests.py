import pytest

from anointments.script_filter import find_anointments


@pytest.mark.django_db
class TestFindAnointments:
    def test_with_one_oil_find_all_that_use_golden(self, golden_anointments):
        find_all = find_anointments({"Golden Oil"})

        assert find_all == golden_anointments

    def test_with_one_oil_find_all_that_use_golden(
        self, silver_or_opalescent_anointments
    ):
        find_all = find_anointments({"Silver Oil", "Opalescent Oil"})

        assert find_all == silver_or_opalescent_anointments

    def test_oil_combinations(self, many_anointments):
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

        assert find_all == many_anointments
