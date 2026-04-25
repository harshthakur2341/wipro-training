from oops.rectangle import Rectangle
from oops.square import Square

sqobj = Square(10)

print(f'Area:{sqobj.calculate_area()} \t Perimeter :{sqobj.calculate_perieter()}')

rectobj = Rectangle(10,5)

print(f'Area:{rectobj.calculate_area()} \t Perimeter :{rectobj.calculate_perieter()}')

