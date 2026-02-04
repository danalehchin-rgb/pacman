class Shape:
    def __init__(self,shape_name):
        self.shape_name=shape_name
    def area(self):
        print(f"{self.shape_name} cannot calculate area because the required dimensions are missing.")
class Rec(Shape):
    def __init__(self,width,height):
        super().__init__("Rectangle")
        self.width=width
        self.height=height
    def area(self):
        area = self.width * self.height
        print(f"Rectangle area is {area}.")

class Square(Rec):
    def __init__(self, side):
        super().__init__(side, side)
        self.shape_name = "Square"
        self.side = side

    def area(self):
        super().area()
        print(f"Square with side {self.side}.")
