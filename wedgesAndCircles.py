#wedges + circles
#10/18/15 Ben Golder and Jeff Trevino
#A two-layer drawing
#layer 1: Gaussian wedges about a grid of center points, one color.
#layer 2: Circles on the same centers, another color.

from chiplotle import *
import random as rn

#portnames -- 
#back usb is /dev/tty.USA19H142P1.1
#front usb is /dev/tty.USA19H141P1.1

plotter = instantiate_plotters()[0]

def drawWedge(x, y):
    print "x", x, "y", y
    plotter.pen_up([(x, y)])
    plotter.pen_down([(x, y)])
    r = int(rn.gauss(1000, 300))
    startAngle = rn.randint(0,360)
    sweepAngle = int(rn.gauss(180, 100))
    print "r", r, "start", startAngle, "sweep", sweepAngle
    plotter.write(hpgl.EW(
        r,
        startAngle,
        sweepAngle
    ))

def drawCircle(x, y):
    r = 200
    plotter.pen_up([(x, y)])
    plotter.pen_down([(x, y)])
    plotter.write(hpgl.CI(
        r
    ))

#first pass
for x in range(-10640, 9720, 1000):
    for y in range(-7640, 7640, 1000):
        drawWedge(x, y)

#--stop plotter--

#second pass
for x in range(-10640, 9720, 1000):
    for y in range(-7640, 7640, 1000):
        drawCircle(x, y)
    
    
    
