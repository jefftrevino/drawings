#wedges + circles
#10/25/15 Ben Golder and Jeff Trevino
#represents a circle by rotating lines at regular intervals around a center.
#then circles are drawn at each line's midpoint.
#insight: not drawing lines nonetheless allows undrawn lines to act as guides.
#last composition made is a ring of Gaussian circles on undrawn lines.

from chiplotle import *
import random as rn
from math import pi

#portnames -- 
#back usb is /dev/tty.USA19H142P1.1
#front usb is /dev/tty.USA19H141P1.1

plotter = instantiate_plotters()[0]
plotter.pen_up([(0,0)])
plotter.goto_origin()
lines = []
#first draw lines and keep track of them
for x in range(100):

    startX = int(rn.gauss(3000, 400))
    endX = int(rn.gauss(6000, 1000))
    theLine = shapes.line((startX, 0), (endX, 0))
    rotation = (x/360.0 * 2*pi)
    transforms.rotate(theLine, rotation)
    lines.append(theLine)
    plotter.pen_up([theLine.points[0]])
    plotter.pen_down([theLine.points[1]])

then draw a circle at the center of each line, in another color.
for line in lines:
    center = line.center
    print "center is:", center
    radius = rn.gauss(50,25)
    plotter.pen_up([center])
    plotter.write(hpgl.WG(
        radius,
        0,
        360
    ))