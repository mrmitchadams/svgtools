#!/usr/bin/env python3

from svgpathtools import svg2paths, Path
import pyclipper
import svgwrite

def svg_path_to_polygon(svg_path):
    # Convert svg_path to a list of points
    points = []
    for segment in svg_path:
        if hasattr(segment, 'start'):
            points.append((segment.start.real, segment.start.imag))
    if points[0] != points[-1]:
        points.append(points[0])
    return points

def polygon_to_svg_path(polygon):
    # Convert a list of points to an SVG path string
    return "M " + " L ".join(f"{x},{y}" for x, y in polygon) + " Z"

def load_svg_paths(file_path):
    # Load and parse SVG paths from file
    paths, _ = svg2paths(file_path)
    return paths

def get_difference_path(path1, path2):
    poly1 = svg_path_to_polygon(path1)
    poly2 = svg_path_to_polygon(path2)
    
    pc = pyclipper.Pyclipper()
    pc.AddPath(poly1, pyclipper.PT_SUBJECT, True)
    pc.AddPath(poly2, pyclipper.PT_CLIP, True)
    difference = pc.Execute(pyclipper.CT_DIFFERENCE)
    
    return difference[0] if difference else None

def draw_difference_path(difference, output_file):
    d = polygon_to_svg_path(difference)
    dwg = svgwrite.Drawing(output_file, profile='tiny')
    dwg.add(dwg.path(d=d, stroke='black', fill='none'))
    dwg.save()

def get_difference_path_from_files(svg_file1, svg_file2, output_file):
    # Load SVG paths from files
    paths1 = load_svg_paths(svg_file1)
    paths2 = load_svg_paths(svg_file2)

    # Currently assumes single path per file
    path1 = paths1[0]
    path2 = paths2[0]

    # Get the difference path
    difference_path = get_difference_path(path1, path2)

    if difference_path:
        # Draw and save the result as a new SVG file
        draw_difference_path(difference_path, output_file)
    else:
        print("No difference found between the paths.")

def test():
    test_svg_file1='./geometric_operations/test_files/test_1.svg'
    test_svg_file2='./geometric_operations/test_files/test_2.svg'
    test_output_file='difference_test_result.svg'
    get_difference_path_from_files(test_svg_file1, test_svg_file2, test_output_file)

if __name__ == '__main__':
    test()