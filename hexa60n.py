#!/usr/bin/env python3

'''
generate the hexa60n svg avatar
'''

# TODO: don't use stroke_width, instead draw full outline of shape including center filled shape with COLOR, then overlay the WHITE hexagons


import sys

import svgwrite


COLOR = "#9199b4"


def hexagon(dwg, x, y, m):
    '''
    generate a hexagon

    '''
    # TODO: polyline with specific edge removed)
    base_shape = ((1,0), (0,1), (0,3), (1,4), (2,3), (2,1), (1,0))
    shape = ((m*a+x,m*b+y) for a,b in base_shape)
    return dwg.polyline(points=shape)


def hexes(image):
    '''
    draw 5 hexes
    '''
    m = 20

    # hex1 polyline
    hexes = image.add(image.g(id="hexes", fill=COLOR, stroke_width=0))
    hexes.add(hexagon(image, 25, 0, m))

    # hex2 polyline
    hexes.add(hexagon(image, 75, 0, m))

    # hex3 polyline
    hexes.add(hexagon(image, 0, 70, m))

    # hex4 polyline
    hexes.add(hexagon(image, 50, 70, m))

    # hex5 polyline
    hexes.add(hexagon(image, 100, 70, m))


def main():
    image = svgwrite.Drawing("hexa60n.svg")

    hexes(image)

    image.save()


if __name__ == "__main__":
    sys.exit(main())
