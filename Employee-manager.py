class Employee:
    def __init__(self,name,year_born,role):
        self.name=name
        self.year_born=year_born
        self.role=role
    def get_role(self):
        return self.role
    def introduce(self):
        print(f"Hello my name is, {self.name}.")

class Manager(Employee):
    def __init__(self,name,year_born,role):
        super().__init__(name,year_born,role)
        self.employee=[] ## רשימת עובדים שהמנהל אחראי עליהם
    def add_emp(self,emp):
        self.employee.append(emp)

def main():
    emp=Employee("lior","2002","bank")
    manager1=Manager("yoav","1998","sport")
    manager2=Manager("avi","1999","sport")

    manager1.add_emp(manager2)
    manager1.add_emp(emp)
    print("employees:")
    for worker in manager1.employee:
        worker.introduce()
main()