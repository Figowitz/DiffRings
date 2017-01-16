""" Main window for all GUI stuff """

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    """ This creates the main window for the diffraction rings program """

    def __init__(self):
        super().__init__()  # Super class constructor
        self.setWindowTitle('Diffraction rings from profile')