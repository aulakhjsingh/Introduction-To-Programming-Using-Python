x, y = eval(input("Enter a point's x- and y-coordinates: "))

# Determine whether the point is inside the triangle
# getting the point of ina line that starts at point

# Get the intersecting point with the hypotenuse side of the triangle
# of a line that starts and points (0, 0) and touches the user points
xIntersect = (-x * (200 * 100)) / (-y * 200 - x * 100)
yIntersect = (-y * (200 * 100)) / (-y * 200 - x * 100)

# Display results
if x > xIntersect and y > yIntersect:
    print('The point is in the triangle.')
else:
    print('The point is not in the triangle.')
