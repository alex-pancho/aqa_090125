import pytest
from hw_16_task_1 import TeamLead

def test_teamlead_attributes():
    team_lead = TeamLead("Oswin Oswald", 1800, "Development", "Python", 11)
    assert hasattr(team_lead, "name")
    assert hasattr(team_lead, "salary")
    assert hasattr(team_lead, "department")
    assert hasattr(team_lead, "programming_language")
    assert hasattr(team_lead, "team_size")
    