""" Tools to process diffraction data into image """

import numpy as np
import matplotlib.pyplot as plt


def interpolate_rings(profile_data, image_size=(512, 512), max_radius = None):
    """
    Returns a grid with profile data interpolated rotationally into rings.

    profile_data - 1D profile to interpolate
    max_radius - How far to interpolate radially. Should be same unit as input x
    image_size - Resolution of image returned. Tuple
    """
    x_profile = profile_data['radius']
    y_profile = profile_data['intensity']
    print(type(profile_data))
    if max_radius is None:
        max_radius = np.max(x_profile)

    # Prepare coordinates
    image_size = np.array(image_size)
    center = np.floor(image_size/2)
    y_grid, x_grid = np.indices(image_size)

    # For each pixel, find distance from center
    r_grid = np.sqrt((x_grid - center[0])**2 + (y_grid - center[1])**2)
    r_grid = np.sqrt(2) * max_radius * r_grid/np.max(r_grid)

    # Go through each line of image and interpolate intensity value at given pixel
    rings_grid = np.zeros(np.shape(r_grid))
    for i, r_line in enumerate(r_grid):
        y0 = np.interp(r_line, x_profile, y_profile)
        rings_grid[i] = y0

    return rings_grid

