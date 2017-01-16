from image_tools import *
from file_tools import *

from gui.main_window import *


def main():
    folder = '/home/nikolaj/Dropbox/DTU/11. semester/Experimentelt projekt/crystaldata/Ni Ga diffraction/'
    file = '103856-ICSD Ni3 Ga Profile.txt'
    file = folder + file

    pdata = import_profile(file)

    rings = interpolate_rings(pdata)
    plt.imshow(rings)
    plt.show()


if __name__ == '__main__':
    main()