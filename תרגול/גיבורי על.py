class Hero:
    def __init__(self, name, alias, age):
        self.name=name
        self.alias=alias
        self.age=age
        self.health=100
        self.level=1
    def get_info(self):
        print(f"The name of the hero- {self.name} \nalias- {self.alias} \nage- {self.age} \nlevel- {self.level}")
    def use_power(self):
        print(f"{self.alias} uses a basic power")
    def move(self,power):
        print(f"{self.alias} movement is- {power}")
    def take_damage(self,damage):
        self.health-=damage
        if self.health<0:
            self.health=0
    def is_alive(self):
        if self.health>0:
            return True
        return False

class SpeedHero(Hero):
    def __init__(self,name,alias,age,max_speed):
        super().__init__(name,alias,age)
        self.max_speed=max_speed
    def dash(self):
        print(f"{self.alias} is sprinting at {self.max_speed} km/h!")

class StrengthHero(Hero):
    def __init__(self, name, alias, age, strength):
        super().__init__(name, alias, age)
        self.strength=strength
    def lift_heavy(self):
        print(f"{self.alias} is lifting a heavy object.")

class Blaze(SpeedHero):
    def __init__(self,name,alias,age,max_speed):
        super().__init__(name,alias,age,max_speed)
    def use_power(self):
        print(f"{self.alias} uses his blazing speed aמd leaves a trail of fire behind!")
    def time_trial(self,direction):
        if direction=='Forward':
            print(f"{self.alias} runs forward through time and lightning speed!")
        elif direction=='Backward':
            print(f"{self.alias} runs back in time, rewriting history in a fiery blur.")

class Swift(SpeedHero):
    def __init__(self, name, alias, age, max_speed):
        super().__init__(name, alias, age,max_speed)
    def use_power(self):
        super().use_power()
        print(f"{self.alias} moves to fast that time itself seems to freeze!")
    def phase_step(self):
        print(f"{self.alias} performs a phase step-disappearing in a flash!")

class WonderWoman(StrengthHero):
    def __init__(self,name,alias,age,strength):
        super().__init__(name,alias,age,strength)
    def use_power(self):
        print(f"{self.alias} unleashes her rage,doubling her strength and shaking the battlefield.")
    def ground_slam(self):
        print(f"{self.alias} uses her ultimate power: a mighty ground slam that shakes the earth.")

class Atlas(StrengthHero):
    def __init__(self, name, alias, age, strength):
        super().__init__(name, alias, age, strength)
    def use_power(self):
        super().use_power()
        print(f"{self.alias} uses his power to summon a personal energy shield around himself.")
    def shield_wall(self):
        print(f"{self.alias} forms a massive shield wall, protecting all his allies harm!")

