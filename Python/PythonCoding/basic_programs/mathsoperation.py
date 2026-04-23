from mypaack.basicshapes import areaofsq, perimeterofsq, areaofrect
from mypaack.circle import areaofcircle, perimeterofcircle

radius = int (input ('Enter radius '))

print(areaofcircle(rad = radius))
print('perimeter', perimeterofcircle(rad = radius))

si = int (input ('Enter side '))
print(areaofsq(side = radius))
print('perimeter', perimeterofsq(side = radius))


l = int (input ('Enter length '))
b = int (input ('Enter breadth '))

print(areaofrect(len=l, brd= b))