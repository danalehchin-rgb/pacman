class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def print_status(self):
        print(f"{self.width}x{self.height} | Area: {self.area()} | Perimeter: {self.perimeter()} | Square? {self.is_square()}")

def main():
    rect1 = Rectangle(4, 6)
    rect2 = Rectangle(5, 5)
    rect1.print_status()
    rect2.print_status()

    area1 = rect1.area()
    area2 = rect2.area()
    if area1 > area2:
        print("Rectangle 1 is larger in area.")
    elif area2 > area1:
        print("Rectangle 2 is larger in area.")
    else:
        print("Both rectangles have the same area.")
    Hekef1 = rect1.perimeter()
    Hekef2 = rect2.perimeter()
    if Hekef1 > Hekef2:
        print("Rectangle 1 is larger in hekef.")
    elif Hekef2 > Hekef1:
        print("Rectangle 2 is larger in hekef.")
    else:
        print("Both rectangles have the same hekef.")
main()