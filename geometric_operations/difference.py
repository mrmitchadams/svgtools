#!/usr/bin/env python3

from svgpathtools import Path
import pyclipper
import svgwrite

import utils.svg_utils as svg_utils

def get_difference_path(path1 : Path, path2 : Path) -> Path:
    poly1 = svg_utils.svg_path_to_polygon(path1)
    poly2 = svg_utils.svg_path_to_polygon(path2)
    
    pc = pyclipper.Pyclipper()
    pc.AddPath(poly1, pyclipper.PT_SUBJECT, True)
    pc.AddPath(poly2, pyclipper.PT_CLIP, True)
    difference = pc.Execute(pyclipper.CT_DIFFERENCE)
    return svg_utils.polygon_to_svg_path(difference[0]) if difference else None

def get_difference_path_from_files(svg_file1, svg_file2, output_file):
    # Load SVG paths from files
    file1_paths, file1_attributes = svg_utils.load_svg_paths_from_file(svg_file1)
    file2_paths, _ = svg_utils.load_svg_paths_from_file(svg_file2)

    # Currently assumes single path per file
    file1_path = file1_paths[0]
    file2_path = file2_paths[0]

    # Get the difference path
    difference_path = get_difference_path(file1_path, file2_path)

    if difference_path:
        new_attributes = file1_attributes
        new_attributes[0] = [{k: file1_attributes[0][0][k] for k in ("style",)}]
        # Draw and save the result as a new SVG file
        # new_attributes = {'style': file1_attributes[1].at('style')}
        svg_utils.save_svg_paths_to_file([difference_path], output_file, new_attributes)
    else:
        print("No difference found between the paths.")

def test():
    test_svg_file1='./geometric_operations/test_files/test_1.svg'
    test_svg_file2='./geometric_operations/test_files/test_2.svg'
    test_output_file='difference_test_result.svg'
    get_difference_path_from_files(test_svg_file1, test_svg_file2, test_output_file)

if __name__ == '__main__':
    test()