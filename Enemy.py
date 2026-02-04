class Enemy:
    def __init__(self,life, power,speed,hands):
        self.life=life
        self.power=power
        self.speed=speed
        self.hands=hands

    def eat(self):
        self.life+=10
        self.power-=5
        print("You ate! your life is:" , self.life , " your power is:" ,self.power)

    def run_forward(self):
        self.power-=15
        self.speed+=7
        print("You ran forward! your power is:",self.power," your speed: ",self.speed)

    def print_status(self):
        print("Status: you life is ",self.life," ,and you power ",self.power)


def main():
    enemy1 = Enemy(100, 40, 20, 2)
    enemy1.eat()
    enemy1.run_forward()
    enemy1.print_status()
main()