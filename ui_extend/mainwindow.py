from PyQt5.QtWidgets import  QMainWindow

from ui import Ui_MainWindow
from ui_extend import InputInfoWidgetEx, CheckWidgetEx, AnalysisWidgetEx, ExportWidgetEx


class MainWindowEx(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindowEx, self).__init__()
        self.setupUi(self)
        self.initTab()

    def initTab(self):
        self.tab_input_info.layout().addWidget(InputInfoWidgetEx())
        self.tab_check.layout().addWidget(CheckWidgetEx())
        self.tab_analysis.layout().addWidget(AnalysisWidgetEx())
        self.tab_export.layout().addWidget(ExportWidgetEx())