import unittest
from homework_16 import TeamLead

class TestTeamLead(unittest.TestCase):
    def setUp(self):
        self.team_lead = TeamLead("Kseniya", 10000, "IT", "Python", 12)

    def test_has_manager_attributes(self):
        self.assertEqual(self.team_lead.name, "Kseniya")
        self.assertEqual(self.team_lead.salary, 10000)
        self.assertEqual(self.team_lead.department, "IT")

    def test_has_developer_attributes (self):
        self.assertEqual(self.team_lead.programming_language, "Python")

    def test_has_teamlead_attributes (self):
        self.assertEqual(self.team_lead.team_size, 12) 

    def test_missing_name(self):
        with self.assertRaises(TypeError):
            TeamLead(None, 10000, "IT", "Python", 12)

    def test_missing_salary(self):
        with self.assertRaises(ValueError):
            TeamLead("Kseniya", None, "IT", "Python", 12)

    def test_missing_department(self):
        with self.assertRaises(TypeError):
            TeamLead("Kseniya", 10000, None, "Python", 12)

    def test_missing_programming_language(self):
        with self.assertRaises(TypeError):
            TeamLead("Kseniya", 10000, "IT", None, 12)

    def test_missing_team_size(self):
        with self.assertRaises(ValueError):
            TeamLead("Kseniya", 10000, "IT", "Python", None)

    def test_missing_all_attributes(self):
        with self.assertRaises(TypeError):
            TeamLead()


if __name__ == "__main__":
    unittest.main()