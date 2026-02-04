class Person:
    def __init__(self, name, age, adress, children):
        self.name = name
        self.age = age
        self.adress = adress
        # אם העבירו רשימת ילדים, נשתמש בה. אם העבירו None, ניצור רשימה ריקה
        if children is None:
            self.children = []
        else:
            self.children = children

    def add_child(self,new_child):
        self.children.append(new_child)
    def print_child_names(self):
        if not self.children:## אם היא ריקה יוצאים מהפונקציה
           return
        for child in self.children:
            print(child.name)
    def print_details(self):
        print("name:", self.name, "\nage:", self.age)
        print("children:")
        self.print_child_names()
def main():
    per1=Person("Gay",14,"tel aviv",None)
    per2=Person("gal",23,"yapo",None)
    per3 = Person("Yohav", 60, "Tel Aviv", None)

    per3.add_child(per1)
    per3.add_child(per2)

    child=Person("Dana",0,"Tel Aviv",None)
    per3.add_child(child)
    per3.print_details()
main()