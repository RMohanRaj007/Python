class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  
        self.salary = salary
        self.post = post
