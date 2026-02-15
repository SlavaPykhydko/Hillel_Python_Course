class Employee:

    def __init__(self, name: str, salary: float, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, department: str, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):

    def __init__(self, programming_language: str, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):

    def __init__(self, team_size: int, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

