import sys
from math import sqrt, cos, sin, pi
def rotateVec(v, angle):
    #rotates a vector ccw by specified angle
    a = (angle / 360) * 2 * pi
    return [v[0] * cos(a) - v[1] * sin(a), v[0] * sin(a) + v[1] * cos(a)]
def makeArc(f, sx, sy, cx, cy, ex, ey):
    #Make a quartic bezier curve based on the following parameters:
    #starting position
    #control point
    #end point
    f.write("<path d=\" M {} {} Q{},{} {},{}\" stroke-width=\"3\" stroke=\"black\" fill=\"none\"/>\n".format(sx, sy, cx, cy, ex, ey))

def startFractal(f, s, v, num, max_iteration):
    generateFractal(f, s, v, 0, 20, max_iteration)

def generateFractal(f, s, v, iteration, angle, max_iteration):
    if(iteration == max_iteration):
        return

    #calculate control point
    # v = rotateVec(v, angle)
    mid = [(2 * s[0] + v[0]) / 2, (2 * s[1] + v[1]) / 2]
    midv1 = [mid[0] - s[0], mid[1] - s[1]]
    #rotate midv by 90 degrees based on whether arcing to the left or right
    # if(angle < 0):
        #arc left
    midv = [midv1[1], -midv1[0]]
    c = [mid[0] + midv[0], mid[1] + midv[1]]
    makeArc(f, s[0], s[1], c[0], c[1], s[0] + v[0], s[1] + v[1])

    # else:
    midv = [-midv[1], midv[0]]
    c = [mid[0] + midv[0], mid[1] + midv[1]]
    makeArc(f, s[0], s[1], c[0], c[1], s[0] + v[0], s[1] + v[1])

    newstart = [s[0] + v[0], s[1] + v[1]]
    newv1 = rotateVec(v, angle)
    newv2 = rotateVec(v, -angle)
    generateFractal(f, newstart, newv1, iteration+1, angle, max_iteration)
    generateFractal(f, newstart, newv2, iteration+1, angle, max_iteration)


if __name__ == '__main__':
    #create svg file of name and fractal pattern
    #fractal generation strategy:
    #have a center line composed of x fractal start points. The number and the length of the line determine the size
    #of each fractal element
    #off of the center line, at each start points generate a fractal by:
    #define a diagonal vector to the start line at an angle such that y number of fractal iterations
    #forms a complete circle. For each iteration, branch in each direction based on the specified angle
    #for a given fractal element: defined by a vector, a start point, and a direction (left or right)

    f = open("fractal.svg", "w")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n")
    f.write("<svg width=\"1000\" height=\"1000\" xmlns=\"http://www.w3.org/2000/svg\">\n")
    startFractal(f, [500, 500], [0, 50], 1, 8)
    startFractal(f, [500, 500], [0, -50], 1, 8)

    f.write("</svg>")
    f.close()
    print("Fractal pattern generated\n")

