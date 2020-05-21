import math

side = eval(input("Enter the side: "))

pi = 3.14159

area = (5 * (side * side)) / (4 * math.tan(pi / 5))

print("The area of the pentagon is ", area)