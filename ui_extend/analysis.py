from PyQt5.QtWidgets import QWidget

from ui import Ui_AnalysisWidget


class AnalysisWidgetEx(Ui_AnalysisWidget, QWidget):
    def __init__(self):
        super(AnalysisWidgetEx, self).__init__()
        self.setupUi(self)
