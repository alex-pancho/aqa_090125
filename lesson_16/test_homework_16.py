import pytest
from homework_16 import TeamLead

def test_lead_has_manager_attr():
    team_lead = TeamLead("Svitlana", 120000, "IT", "Python", 5)
    assert hasattr(team_lead, "department")

def test_lead_has_developer_attr():
    team_lead = TeamLead("Mark", 80000, "Product", "Java", 9)
    assert hasattr(team_lead, "programming_language")

def test_lead_has_team_size():
    team_lead = TeamLead("Svitlana", 120000, "IT", "Python", 5)
    assert hasattr(team_lead, "team_size")

def test_invalid_salary_type():
    with pytest.raises(ValueError, match="Salary must be a number."):
        TeamLead("Mark", "eighty thousand", "Product", "Java", 9)

def test_invalid_team_size_type():
    with pytest.raises(ValueError, match="Team size must be an integer."):
        TeamLead("Mark", 80000, "Product", "Java", "five")

def test_missing_arguments():
    with pytest.raises(TypeError):
        TeamLead("Mark", 80000)

def test_non_existent_attribute():
    team_lead = TeamLead("Svitlana", 120000, "IT", "Python", 5)
    assert not hasattr(team_lead, "age")

if __name__ == "__main__":
    pytest.main(["-v", __file__])