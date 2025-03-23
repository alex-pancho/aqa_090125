
class Employee:

    def __init__(self, name:str, salary):
        self.name = name.title()
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department:str):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size
