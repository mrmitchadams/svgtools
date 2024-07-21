#!/usr/bin/env python3

from svgpathtools import svg2paths2, Path, wsvg, Line

def load_svg_paths_from_file(filename : str) -> list[Path]:
    # Load and parse SVG paths from file
    paths, attributes, svg_attributes = svg2paths2(filename)
    return paths, [attributes, svg_attributes]

def save_svg_paths_to_file(paths, filename, attributes=None):
    #wsvg(paths, attributes=attributes, svg_attributes=svg_attributes, filename=filename)
    if attributes:
        wsvg(paths, attributes=attributes[0], svg_attributes=attributes[1], filename=filename)
    else:
        wsvg(paths, filename=filename)

def svg_path_to_polygon(svg_path : Path):
    # Convert svg_path to a list of points
    points = []
    for segment in svg_path:
        if hasattr(segment, 'start'):
            points.append((segment.start.real, segment.start.imag))
    if points[0] != points[-1]:
        points.append(points[0])
    return points

def polygon_to_svg_path(polygon):
    if polygon[0] != polygon[-1]:
        polygon.append(polygon[0])
    # Create a list of Line segments connecting each point
    segments = [Line(start=complex(polygon[i][0], polygon[i][1]), 
                     end=complex(polygon[i+1][0], polygon[i+1][1]))
                for i in range(len(polygon) - 1)]
    # Return a Path object containing these segments
    return Path(*segments)

