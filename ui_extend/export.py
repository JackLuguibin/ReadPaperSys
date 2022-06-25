from PyQt5.QtWidgets import QWidget

from ui import Ui_ExportWidget


class ExportWidgetEx(Ui_ExportWidget, QWidget):
    def __init__(self):
        super(ExportWidgetEx, self).__init__()
        self.setupUi(self)
