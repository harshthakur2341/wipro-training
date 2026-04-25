from oops.formulamethods import FM


class Square(FM):
    def __init__(self,s):
        self.side = s


    def calculate_area(self):
        return self.side * self.side

    def calculate_perieter(self):
        return 4 * self.side

