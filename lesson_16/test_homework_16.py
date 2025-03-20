import unittest
from homework_16 import TeamLead 

class TestTeamLead(unittest.TestCase):

    def setUp(self):
        self.team_lead = TeamLead('John', 5000, 'IT', 'Python', 5)

    def test_01_has_name_attribute(self):
        self.assertTrue(hasattr(self.team_lead, "name"))
        self.assertEqual(self.team_lead.name, "John")

    def test_02_has_salary_attribute(self):
        self.assertTrue(hasattr(self.team_lead, "salary"))
        self.assertEqual(self.team_lead.salary, 5000)

    def test_03_has_department_attribute(self):
        self.assertTrue(hasattr(self.team_lead, "department"))
        self.assertEqual(self.team_lead.department, "IT")

    def test_04_has_programming_language_attribute(self):
        self.assertTrue(hasattr(self.team_lead, "programming_language"))
        self.assertEqual(self.team_lead.programming_language, "Python")

    def test_05_has_team_size_attribute(self):
        self.assertTrue(hasattr(self.team_lead, "team_size"))
        self.assertEqual(self.team_lead.team_size, 5)



if __name__ == "__main__":
    unittest.main(verbosity=2)