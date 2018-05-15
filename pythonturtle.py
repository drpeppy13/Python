import turtle
# the distance we want the pointer to travel each time
DIST = 50
for x in range(15,30):
    print "x", x
    for y in range(14,30):
        print "y", y
        # turn the pointer 270 degrees to the right
        turtle.right(270)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 10