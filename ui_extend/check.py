from PyQt5.QtWidgets import QWidget

from ui import Ui_CheckWidget


class CheckWidgetEx(Ui_CheckWidget, QWidget):
    def __init__(self):
        super(CheckWidgetEx, self).__init__()
        self.setupUi(self)
