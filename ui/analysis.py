# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnalysisWidget(object):
    def setupUi(self, AnalysisWidget):
        AnalysisWidget.setObjectName("AnalysisWidget")
        AnalysisWidget.resize(827, 547)
        self.verticalLayout = QtWidgets.QVBoxLayout(AnalysisWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(AnalysisWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(AnalysisWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(AnalysisWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(AnalysisWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(AnalysisWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(AnalysisWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(AnalysisWidget)
        QtCore.QMetaObject.connectSlotsByName(AnalysisWidget)

    def retranslateUi(self, AnalysisWidget):
        _translate = QtCore.QCoreApplication.translate
        AnalysisWidget.setWindowTitle(_translate("AnalysisWidget", "Form"))
        self.label_2.setText(_translate("AnalysisWidget", "分析界面"))
        self.label.setText(_translate("AnalysisWidget", "选择班级："))
        self.pushButton.setText(_translate("AnalysisWidget", "开始分析"))
        self.groupBox.setTitle(_translate("AnalysisWidget", "分数分布图"))
        self.groupBox_2.setTitle(_translate("AnalysisWidget", "分数档次分布"))