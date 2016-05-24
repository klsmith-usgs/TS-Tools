# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lcmap\TSTools-master\tstools\ui\ui_config.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName(_fromUtf8("Config"))
        Config.resize(700, 550)
        self.gridLayout = QtGui.QGridLayout(Config)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.combox_ts_model = QtGui.QComboBox(Config)
        self.combox_ts_model.setObjectName(_fromUtf8("combox_ts_model"))
        self.gridLayout.addWidget(self.combox_ts_model, 3, 0, 1, 2)
        self.lab_config = QtGui.QLabel(Config)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lab_config.setFont(font)
        self.lab_config.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_config.setObjectName(_fromUtf8("lab_config"))
        self.gridLayout.addWidget(self.lab_config, 0, 0, 1, 2)
        self.line = QtGui.QFrame(Config)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.edit_location = QtGui.QLineEdit(Config)
        self.edit_location.setObjectName(_fromUtf8("edit_location"))
        self.horizontalLayout.addWidget(self.edit_location)
        self.button_location = QtGui.QPushButton(Config)
        self.button_location.setObjectName(_fromUtf8("button_location"))
        self.horizontalLayout.addWidget(self.button_location)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.lab_location = QtGui.QLabel(Config)
        self.lab_location.setObjectName(_fromUtf8("lab_location"))
        self.gridLayout.addWidget(self.lab_location, 5, 0, 1, 2)
        self.button_box = QtGui.QDialogButtonBox(Config)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 10, 1, 1, 1)
        self.line_2 = QtGui.QFrame(Config)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)
        self.label_4 = QtGui.QLabel(Config)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.widget = QtGui.QWidget(Config)
        self.widget.setMinimumSize(QtCore.QSize(0, 300))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.custom_widget = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_widget.sizePolicy().hasHeightForWidth())
        self.custom_widget.setSizePolicy(sizePolicy)
        self.custom_widget.setMinimumSize(QtCore.QSize(250, 200))
        self.custom_widget.setObjectName(_fromUtf8("custom_widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.custom_widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.custom_widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.info_widget = QtGui.QWidget(self.splitter)
        self.info_widget.setMinimumSize(QtCore.QSize(200, 200))
        self.info_widget.setObjectName(_fromUtf8("info_widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.info_widget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.info_widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.splitter)
        self.gridLayout.addWidget(self.widget, 7, 0, 1, 2)

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        Config.setWindowTitle(_translate("Config", "Dialog", None))
        self.lab_config.setText(_translate("Config", "Dataset Configuration", None))
        self.button_location.setText(_translate("Config", "Open", None))
        self.lab_location.setText(_translate("Config", "Stacked time series location:", None))
        self.label_4.setText(_translate("Config", "Time Series Type:", None))
        self.label.setText(_translate("Config", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Configuration</span></p></body></html>", None))
        self.label_2.setText(_translate("Config", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Information</span></p></body></html>", None))

