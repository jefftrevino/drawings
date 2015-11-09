#branching lines
#11/8/15 Ben Golder and Jeff Trevino

from chiplotle import *
from chiplotle.tools.mathtools.polar_to_xy import polar_to_xy
from chiplotle.tools.mathtools.xy_to_polar import xy_to_polar
import random as rn
from math import pi

plotter = instantiate_plotters()[0]
plotter.pen_up([(0,0)])

def getLineLength(level):
    levelInverse = LEVELS - level
    safetyLevel = 5.0
    levelDefault = 5000 ** ((levelInverse + safetyLevel) / (LEVELS + safetyLevel))
    variance = rn.gauss(0, .05 * levelDefault)
    length = levelDefault - variance
    return length

def interpolate(howFar, start, end):
    return end * howFar + start * (1 - howFar)

def choosePointOnLine(line, howFar):
    startCoord = line.points[0]
    endCoord = line.points[1]
    x = interpolate(howFar, startCoord[0], endCoord[0])
    y = interpolate(howFar, startCoord[1], endCoord[1])
    return [x,y]

def findRelativeAngle(parent, angle):
    # deterine the parent angle
    # adjust with child angles
    x = parent.points[1].x - parent.points[0].x
    y = parent.points[1].y - parent.points[0].y
    r, parentAngle = xy_to_polar([x, y])
    radians = (angle/360.0 * 2*pi)
    return parentAngle + radians

def makeLine(level, angle, parent_param, parent=None):
    length = getLineLength(level)
    if parent:
        startPoint = [int(n) for n in choosePointOnLine(parent, parent_param)]
        angle = findRelativeAngle(parent, angle)
    else:
        startPoint = [0,0]
    x, y = polar_to_xy([length, angle])
    x += startPoint[0]
    y += startPoint[1]
    x = int(x)
    y = int(y)
    line = shapes.line(
        startPoint,
        [x, y]
    )
    print "drawing line at level", level, "from", startPoint, "to", [x,y]
    for i in range(LEVELS - level):
        plotter.pen_up([startPoint])
        plotter.pen_down([(x,y)])
    return line

def makeChildren(level, parent=None):
    n_branches = rn.randint(3,4)    
    if parent:
        childAngles = rn.sample([45, -45, 45, -45], n_branches)
    else:
        childAngles = rn.sample([45, -45, 135, -135], n_branches)
    branchPoints = rn.sample([.7, .8, .85, .9, .95], n_branches)
    for angle, branchPoint in zip(childAngles, branchPoints):
        line = makeLine(level, angle, branchPoint, parent)
        BRANCHES[level].append(line)

def makeLevel(level):
    parents = BRANCHES[level - 1]
    for parent in parents:
        makeChildren(level, parent)

def makeDrawing(numLevels):
    for i in range(numLevels):
        BRANCHES[i] = []
    #choose root parents
    makeChildren(0)
    for i in range(1, numLevels):
        makeLevel(i)
        
BRANCHES = {}
LEVELS = 4
makeDrawing(LEVELS)