#!/usr/bin/env python3

'''
generate the hexa60n svg avatar
'''


import sys

import svgwrite


COLOR = "#9199b4"


def main():
    image = svgwrite.Drawing("hexa60n.svg")

    lines = image.add(image.g(id="lines", stroke=COLOR, fill="white", stroke_width=3))

    lines.add(image.polygon(points=[(5,0), (0,5), (0,10), (5,15), (10,10), (10,5), (5,0)]))

    image.save()


if __name__ == "__main__":
    sys.exit(main())
