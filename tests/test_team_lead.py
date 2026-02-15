import os
print("Current working dir:", os.getcwd())

from lesson_10.homework_10_1 import Employee, Manager, Developer, TeamLead
import pytest

def test_team_lead_inheritance():
    assert issubclass(TeamLead, Manager)
    assert issubclass(TeamLead, Developer)
    assert issubclass(TeamLead, Employee)


def test_team_lead_attributes_values():
    tl = TeamLead(
        name="John",
        salary=5000,
        department="IT",
        programming_language="Python",
        team_size=5
    )

    assert isinstance(tl, Manager)
    assert isinstance(tl, Developer)
    assert isinstance(tl, Employee)

    assert tl.name == "John"
    assert tl.salary == 5000
    assert tl.department == "IT"
    assert tl.programming_language == "Python"
    assert tl.team_size == 5
