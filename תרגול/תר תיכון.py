class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print("My name is ",self.name)

class Student(Person):
    def __init__(self, name,school):
        super().__init__(name)
        self.school=school
    def introduce(self):
        super().introduce()
        print("l study at ", self.school)

class HighSchoolStudent(Student):
    def __init__(self,name,school,grade):
        super().__init__(name, school)
        self.grade=grade

    def introduce(self):
        super().introduce()
        print("I am in grade", self.school)