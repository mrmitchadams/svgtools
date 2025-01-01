#!/usr/bin/env python3

from svgpathtools import Path
import pyclipper
import svgwrite
import utils.svg_utils as svg_utils

def get_union_paths(paths : list[Path]) -> list[Path]:
    polygons = [svg_utils.svg_path_to_polygon(path) for path in paths]
    pc = pyclipper.Pyclipper()
    union_polys = [polygons[0]]
    for poly in polygons[1:]:
        pc.Clear()
        for polysubj in union_polys:
            pc.AddPath(polysubj, pyclipper.PT_SUBJECT, True)
        pc.AddPath(poly, pyclipper.PT_CLIP, True)
        union_polys = pc.Execute(pyclipper.CT_UNION)
    union_paths = [svg_utils.polygon_to_svg_path(poly) for poly in union_polys]
    return union_paths

def get_union_path_from_files(svg_files : list[str], output_file : str):
    # Load SVG paths from files
    paths_from_files = []
    path_attributes = []
    for file in svg_files:
        paths, attributes = svg_utils.load_svg_paths_from_file(file)
        paths_from_files += paths #todo: account for holes (and clip them) using path.is_contained_by
        path_attributes.append(attributes)

    # Get the union path
    union_paths = get_union_paths(paths_from_files)

    if union_paths:
        # new_attributes = path_attributes[0]
        # new_attributes[0] = [{k: path_attributes[0][0][0][k] for k in ("style",)}]
        # OR new_attributes = {'style': path_attributes[0][1].at('style')}
        svg_utils.save_svg_paths_to_file(union_paths, output_file)
    else:
        print("No union_path found between the paths.")

def test():
    svg_files = ['test_1.svg', 'test_2.svg', 'test_3.svg', 'test_4.svg']
    svg_files = ['./geometric_operations/test_files/' + file for file in svg_files]
    test_output_file='union_test_result.svg'
    get_union_path_from_files(svg_files, test_output_file)

if __name__ == '__main__':
    test()