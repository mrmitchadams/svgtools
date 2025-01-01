from svgpathtools import Path
import utils.svg_utils as svg_utils


def rectangle(width, height, origin=[0,0]) -> Path:
    points = []
    points.append(origin)
    points.append([origin[0]+width, origin[1]])
    points.append([origin[0]+width, origin[1]+height])
    points.append([origin[0], origin[1]+height])
    return svg_utils.polygon_to_svg_path(points)
