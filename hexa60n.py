#!/usr/bin/env python3

'''
generate the hexa60n svg avatar
'''


import sys

import svgwrite


def main():
    image = svgwrite.Drawing("hexa60n.svg")

    lines = image.add(image.g(id="lines", stroke="#9199b4", stroke_width=3))

    lines.add(image.line(start=(5, 0), end=(0, 5)))
    lines.add(image.line(start=(0, 5), end=(0, 10)))
    lines.add(image.line(start=(0, 10), end=(5, 15)))
    lines.add(image.line(start=(5, 15), end=(10, 10)))
    lines.add(image.line(start=(10, 10), end=(10, 5)))
    lines.add(image.line(start=(10, 5), end=(5, 0)))

    image.save()


if __name__ == "__main__":
    sys.exit(main())
