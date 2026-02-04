class Battery:
    def __init__(self):
        self.percentage=100

    def get_percentage(self):
        return self.percentage

    def use_battery(self,per_to_use):
        if self.percentage >= per_to_use:
            self.percentage = self.percentage - per_to_use
            print("new percentage ",self.percentage)
        else:
            print("not enough battery ")

def main():
    battery = Battery()
    battery.use_battery(50)
    battery.use_battery(65)
    print("current percentage ",battery.get_percentage())
main()