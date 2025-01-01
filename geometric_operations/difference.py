#!/usr/bin/env python3

from svgpathtools import Path
import pyclipper
import svgwrite
import utils.svg_utils as svg_utils

def get_difference_paths(subject_path : Path, clip_paths : list[Path]) -> list[Path]:
    subj_poly = svg_utils.svg_path_to_polygon(subject_path)
    clip_polys = [svg_utils.svg_path_to_polygon(path) for path in clip_paths]
    pc = pyclipper.Pyclipper()
    difference_polygons = [subj_poly]
    for poly in clip_polys:
        pc.Clear()
        for polysubj in difference_polygons:
            pc.AddPath(polysubj, pyclipper.PT_SUBJECT, True)
        pc.AddPath(poly, pyclipper.PT_CLIP, True)
        difference_polygons = pc.Execute(pyclipper.CT_DIFFERENCE)
    difference_paths = [svg_utils.polygon_to_svg_path(poly) for poly in difference_polygons]
    return difference_paths

def get_difference_paths_from_files(subject_svg_file, clip_svg_files : list[str], output_file : str):
    # Load SVG paths from files
    subject_file_paths, subject_file_attributes = svg_utils.load_svg_paths_from_file(subject_svg_file)
    clip_file_paths = []
    for file in clip_svg_files:
        file_paths,_ =svg_utils.load_svg_paths_from_file(file)
        clip_file_paths += file_paths

    # get the difference paths
    difference_paths = []
    for subj_path in subject_file_paths:
        difference_paths += get_difference_paths(subj_path, clip_file_paths)
        
    if difference_paths:
        # new_attributes = subject_file_attributes
        # new_attributes[0] = [{k: subject_file_attributes[0][0][k] for k in ("style",)}]
        svg_utils.save_svg_paths_to_file(difference_paths, output_file)
    else:
        print("No difference found between the paths.")

def test():
    subject_svg_file = './geometric_operations/test_files/test_1.svg'
    clip_svg_files = ['test_2.svg', 'test_3.svg', 'test_4.svg']
    clip_svg_files = ['./geometric_operations/test_files/' + file for file in clip_svg_files]
    test_output_file='difference_test_result.svg'
    get_difference_paths_from_files(subject_svg_file, clip_svg_files, test_output_file)

if __name__ == '__main__':
    test()