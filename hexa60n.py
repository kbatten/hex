#!/usr/bin/env python3

'''
generate the hexa60n svg avatar
'''

# TODO: don't use stroke_width, instead draw full outline of shape including center filled shape with COLOR, then overlay the WHITE hexagons


import sys

import svgwrite


COLOR = "#9199b4"


def hexagon(x, y, m):
    '''
    generate a hexagon

    '''
    base_shape = ((1,0), (0,1), (0,3), (1,4), (2,3), (2,1), (1,0))
    return [(m*a+x,m*b+y) for a,b in base_shape]

def hexagon_poly(dwg, x, y, m):
    return dwg.polyline(points=hexagon(x, y, m))


def intersect(p1, p2):
    '''
    calculates a specific intersection of 45 degree lines
     the first coord is on the line going y+
     the second coord is the line going y-
    '''
    b1 = p1[1] - p1[0]
    b2 = p2[1] + p2[0]

    x = (b2 - b1) / 2
    y = x + b1
    return (x, y)


def hexes(image):
    '''
    draw 5 hexes
    '''

    m = 20

    # hex1 polyline
    hexes = image.add(image.g(id="hexes", fill=COLOR, stroke_width=0))
    #hexes.add(hexagon_poly(image, 25, 0, m))

    # hex2 polyline
    #hexes.add(hexagon_poly(image, 75, 0, m))

    # hex3 polyline
    #hexes.add(hexagon_poly(image, 0, 70, m))

    # hex4 polyline
    #hexes.add(hexagon_poly(image, 50, 70, m))

    # hex5 polyline
    #hexes.add(hexagon_poly(image, 100, 70, m))

    # TODO: use the coordinates from hexagon
    #       still need to get a point to create the 45 degree bar
    # find crossover between hex3[1,6] and hex1[4,5]
    # (20, 70), (40, 90) x (45, 80), (65, 60)
    # y = x + 50
    # y = -x + 125
    # x + 50 = -x + 125
    # 2x = 125 - 50 = 75
    # x = 37.5
    # y = 87.5


    # coordinates are ccw starting at the top (lowest y value)
    h0 = [(45, 0), (25, 20), (25, 60), (45, 80), (65, 60), (65, 20), (45, 0)]
    h1 = [(95, 0), (75, 20), (75, 60), (95, 80), (115, 60), (115, 20), (95, 0)]
    h2 = [(20, 70), (0, 90), (0, 130), (20, 150), (40, 130), (40, 90), (20, 70)]
    h3 = [(70, 70), (50, 90), (50, 130), (70, 150), (90, 130), (90, 90), (70, 70)]
    h4 = [(120, 70), (100, 90), (100, 130), (120, 150), (140, 130), (140, 90), (120, 70)]

    inter1 = intersect(h2[0], h0[3])
    inter2 = intersect(h1[2], h3[0])

    lines = [h0[0], h0[1], h0[2], h0[3], inter1, h2[0], h2[1], h2[2], h2[3], h2[4],
             h3[2], h3[3], h3[4], h3[5], h3[0],
             inter2, h1[3], h1[4], h1[5], h1[0], h1[1], h0[5], h0[0]]
    hexes.add(image.polygon(points=lines))
    hexes.add(image.polygon(points=h4))


def main():
    image = svgwrite.Drawing("hexa60n.svg")

    hexes(image)

    image.save()


if __name__ == "__main__":
    sys.exit(main())
