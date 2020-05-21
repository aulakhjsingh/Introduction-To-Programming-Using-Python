import math

pi = 3.14159

n = eval(input("Enter the number of sides: "))

s = eval(input("Enter the lenght of sides: "))

area = (n * (s * s)) / (4 * math.tan(pi / n))

print("The area of the polygon is ", area)