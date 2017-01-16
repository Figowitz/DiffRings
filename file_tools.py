""" Tools for importing and exporting files """

import numpy as np


def import_profile(file):
    """ Imports profile from text file in common format (tab delimiter, csv, etc.).
    Data should be in columns as: radius, intensity.
    Returns data as """

    names = ['radius', 'intensity']
    profile_data = np.genfromtxt(file, names=names)

    return profile_data
