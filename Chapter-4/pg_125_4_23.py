x, y = eval(input('Enter a point with two coordinates: '))
w = eval(input('Enter a width of the rectangle: '))
h = eval(input('Enter a height of the rectangle: '))

if x <= (w / 2) and y <= (h / 2):
    print('Point (', x, ',', y, ') is in the rectangle')
else:
    print('Point (', x, ',', y, ') is not in the rectangle')