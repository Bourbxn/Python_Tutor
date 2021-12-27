import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
d = float(input("Enter d: "))
rectArea = x * y
circleArea = math.pi*((d/2)**2)
leftArea = rectArea - circleArea
print("The area of lawn is %.2f sq.m."%leftArea)
