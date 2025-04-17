class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        
        Manager.__init__(self, name, salary, department)
        
        self.programming_language = programming_language
        self.team_size = team_size

def test_teamlead_attributes():
    team_lead = TeamLead
    name="John Doe",
    salary=100000,
    department="Engineering",
    programming_language="Python",
    team_size=5

    assert hasattr(team_lead, 'name')
    assert hasattr(team_lead, 'salary')
    assert hasattr(team_lead, 'department')
    assert hasattr(team_lead, 'programming_language')
    assert hasattr(team_lead, 'team_size')
    assert team_lead.name == "John Doe"
    assert team_lead.salary == 100000
    assert team_lead.department == "Engineering"
    assert team_lead.programming_language == "Python"
    assert team_lead.team_size == 5
    
    print("All tests passed!")
