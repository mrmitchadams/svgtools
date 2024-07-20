#!/usr/bin/env python3

from ..geometric_operations.difference import get_difference_path, load_svg_paths, draw_difference_path

# File paths for the input SVG files
svg_file1 = '/Users/tedhansen/Downloads/test_1.svg'
svg_file2 = '/Users/tedhansen/Downloads/test_2.svg'

# Load SVG paths from files
paths1 = load_svg_paths(svg_file1)
paths2 = load_svg_paths(svg_file2)

# Assuming single path per file, otherwise adjust the logic accordingly
path1 = paths1[0]
path2 = paths2[0]

# Get the difference path
difference_path = get_difference_path(path1, path2)

if difference_path:
    # Draw and save the result as a new SVG file
    draw_difference_path(difference_path, 'difference_result.svg')
else:
    print("No difference found between the paths.")

















# import svgwrite
# from svgpathtools import svg2paths, Path, wsvg

# def load_svg_paths(file_path):
#     paths, attributes = svg2paths(file_path)
#     return paths

# def get_intersection_path(path1, path2):
#     intersections = path1.intersect(path2)
#     print(f"intersections: {intersections}")
#     intersection_points = [seg for seg in intersections]
    
#     if not intersection_points:
#         return None
    
#     combined_path = Path()
#     for seg in intersection_points:
#         print(f"seg: {seg}")
#         combined_path.append(seg)
#     return combined_path

# def write_svg(paths, output_file):
#     dwg = svgwrite.Drawing(output_file, profile='tiny')
#     for path in paths:
#         dwg.add(dwg.path(d=path.d(), fill='none', stroke='black'))
#     dwg.save()

# # File paths for the input SVG files
# svg_file1 = '/Users/tedhansen/Downloads/test_1.svg'
# svg_file2 = '/Users/tedhansen/Downloads/test_2.svg'

# # Load SVG paths from files
# paths1 = load_svg_paths(svg_file1)
# paths2 = load_svg_paths(svg_file2)

# # Assuming single path per file, otherwise adjust the logic accordingly
# path1 = paths1[0]
# path2 = paths2[0]

# # Get the intersection path
# intersection_path = get_intersection_path(path1, path2)

# if intersection_path:
#     # Write the result to a new SVG file
#     write_svg([intersection_path], 'combined_intersection.svg')
# else:
#     print("No intersection found between the paths.")
