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
    