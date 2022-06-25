from PyQt5.QtWidgets import QWidget

from ui import Ui_InputInfoWidget


class InputInfoWidgetEx(Ui_InputInfoWidget, QWidget):
    def __init__(self):
        super(InputInfoWidgetEx, self).__init__()
        self.setupUi(self)
