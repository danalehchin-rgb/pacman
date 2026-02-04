class Pen:
    def __init__(self,color):
        self.color=color
        self.is_open=False
    def open_pen(self):
        self.is_open=True
    def close_pen(self):
        self.is_open=False

    def print_status(self):
        if self.is_open:
            print(f"{self.color} pen: open")
        else:
            print(f"{self.color} pen: close")
def main():
    blue_pen = Pen("Blue")
    black_pen = Pen("Black")
    blue_pen.open_pen()
    blue_pen.print_status()
    black_pen.print_status()
main()