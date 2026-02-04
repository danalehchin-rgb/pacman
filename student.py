class Student:
    def __init__(self,name):
        self.name=name
        self.grades=[]
    def add_grade(self,g):
        self.grades.append(g)
    def get_avg(self):
        if not self.grades:
            return 0
        sum = 0
        for grade in self.grades:
            sum += grade
        return sum / len(self.grades)
    def print_status(self):
        avg = self.get_avg()
        num_of_grades = len(self.grades)
        print(f"Student Name: {self.name}")
        print(f"Number of grades: {num_of_grades}")
        print(f"Average: {avg}")