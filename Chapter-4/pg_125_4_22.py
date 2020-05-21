x, y = eval(input('Enter a point with two coordinates: '))
r = eval(input('Enter the radius of the circle: '))

if ((((x - 0)**2) + ((y - 0)**2))**0.5) <= r:
    print('Point (', x, ',', y, ') is in the circle.')
else:
    print('Point (', x, ',', y, ') is not in the circle.')