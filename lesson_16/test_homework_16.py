import pytest

from homework_16 import TeamLead, get_figure_area_and_perimeter


@pytest.fixture(scope="class")
def obj():
    lead = TeamLead("Dima", 1000, "Development", "Python", 5)
    return lead


class TestTeamLead:

    def test_employee_attributes(self, obj):
        assert hasattr(obj, "name"), "name attr is missing"
        assert hasattr(obj, "salary"), "salary attr is missing"

        assert getattr(obj, "name") == "Dima", "wrong name value"
        assert getattr(obj, "salary") == 1000, "wrong salary value"

    def test_manager_attributes(self, obj):
        assert hasattr(obj, "department"), "department attr is missing"
        assert getattr(obj, "department") == "Development", "wrong department value"

    def test_developer_attributes(self, obj):
        assert hasattr(obj, "programming_language"), "programming_language attr is missing"
        assert getattr(obj, "programming_language") == "Python", "wrong programming_language value"

    def test_team_lead_attributes(self, obj):
        assert hasattr(obj, "team_size"), "team_size attr is missing"
        assert getattr(obj, "team_size") == 5, "wrong team_size value"


class TestFigure:

    @pytest.mark.parametrize(
        "figure",
        [
            {"name": "Square", "data": (2, 2), "res": "Square: Площа = 4.00, Периметр = 8.00"},
            {"name": "Circle", "data": (5,), "res": "Circle: Площа = 78.54, Периметр = 31.42"},
            {"name": "Triangle", "data": (3, 4, 5), "res": "Triangle: Площа = 6.00, Периметр = 12.00"},
        ],
        ids=lambda f: f["name"]
    )
    def test_figure_area_and_perimeter(self, figure):
        res = get_figure_area_and_perimeter(figure["name"], *figure["data"])
        assert res == figure["res"], "Wrong response data"
