import unittest
from hw_16_1 import TeamLead


class TestTeamLead(unittest.TestCase):
    def test_team_lead_attributes(self):
        lead = TeamLead("Alice", 120000, "Software", "Python", 5)
        
        self.assertEqual(lead.name, "Alice")
        self.assertEqual(lead.salary, 120000)
        self.assertEqual(lead.department, "Software")
        self.assertEqual(lead.programming_language, "Python")
        self.assertEqual(lead.team_size, 5)

    def test_team_lead_inheritance(self):
        lead = TeamLead("Alice", 120000, "Software", "Python", 5)
        
        # Check if TeamLead is an instance of Manager and Developer
        self.assertIsInstance(lead, TeamLead)

        # Check if TeamLead has attributes from both Manager and Developer
        self.assertTrue(hasattr(lead, "department"))
        self.assertTrue(hasattr(lead, "programming_language"))
        self.assertTrue(hasattr(lead, "team_size"))
        self.assertTrue(hasattr(lead, "name"))
        self.assertTrue(hasattr(lead, "salary"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
