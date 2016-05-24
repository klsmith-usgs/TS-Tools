# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lcmap\TSTools-master\tstools\ui\ui_series_exporter_item.ui'
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

class Ui_SeriesExporterItem(object):
    def setupUi(self, SeriesExporterItem):
        SeriesExporterItem.setObjectName(_fromUtf8("SeriesExporterItem"))
        SeriesExporterItem.resize(580, 73)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SeriesExporterItem.sizePolicy().hasHeightForWidth())
        SeriesExporterItem.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(SeriesExporterItem)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.but_browse = QtGui.QPushButton(SeriesExporterItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_browse.sizePolicy().hasHeightForWidth())
        self.but_browse.setSizePolicy(sizePolicy)
        self.but_browse.setObjectName(_fromUtf8("but_browse"))
        self.gridLayout.addWidget(self.but_browse, 3, 3, 1, 1)
        self.cbox_enable = QtGui.QCheckBox(SeriesExporterItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbox_enable.sizePolicy().hasHeightForWidth())
        self.cbox_enable.setSizePolicy(sizePolicy)
        self.cbox_enable.setObjectName(_fromUtf8("cbox_enable"))
        self.gridLayout.addWidget(self.cbox_enable, 0, 1, 1, 3)
        self.lab_series = QtGui.QLabel(SeriesExporterItem)
        self.lab_series.setObjectName(_fromUtf8("lab_series"))
        self.gridLayout.addWidget(self.lab_series, 0, 0, 1, 1)
        self.edit_path = QtGui.QLineEdit(SeriesExporterItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_path.sizePolicy().hasHeightForWidth())
        self.edit_path.setSizePolicy(sizePolicy)
        self.edit_path.setObjectName(_fromUtf8("edit_path"))
        self.gridLayout.addWidget(self.edit_path, 3, 1, 1, 2)
        self.label = QtGui.QLabel(SeriesExporterItem)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.retranslateUi(SeriesExporterItem)
        QtCore.QMetaObject.connectSlotsByName(SeriesExporterItem)

    def retranslateUi(self, SeriesExporterItem):
        SeriesExporterItem.setWindowTitle(_translate("SeriesExporterItem", "Form", None))
        self.but_browse.setText(_translate("SeriesExporterItem", "Browse", None))
        self.cbox_enable.setText(_translate("SeriesExporterItem", "CheckBox", None))
        self.lab_series.setText(_translate("SeriesExporterItem", "TextLabel", None))
        self.label.setText(_translate("SeriesExporterItem", "Destination", None))

