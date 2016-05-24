# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lcmap\TSTools-master\tstools\ui\ui_series_exporter.ui'
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

class Ui_SeriesExporter(object):
    def setupUi(self, SeriesExporter):
        SeriesExporter.setObjectName(_fromUtf8("SeriesExporter"))
        SeriesExporter.resize(500, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SeriesExporter.sizePolicy().hasHeightForWidth())
        SeriesExporter.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(SeriesExporter)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scroll_area = QtGui.QScrollArea(SeriesExporter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())
        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName(_fromUtf8("scroll_area"))
        self.scroll_area_contents = QtGui.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 480, 247))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area_contents.sizePolicy().hasHeightForWidth())
        self.scroll_area_contents.setSizePolicy(sizePolicy)
        self.scroll_area_contents.setObjectName(_fromUtf8("scroll_area_contents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scroll_area_contents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.scroll_area_contents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.line = QtGui.QFrame(self.scroll_area_contents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.gridLayout.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.button_box = QtGui.QDialogButtonBox(SeriesExporter)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 1, 0, 1, 1)

        self.retranslateUi(SeriesExporter)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), SeriesExporter.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), SeriesExporter.reject)
        QtCore.QMetaObject.connectSlotsByName(SeriesExporter)

    def retranslateUi(self, SeriesExporter):
        SeriesExporter.setWindowTitle(_translate("SeriesExporter", "Dialog", None))
        self.label.setText(_translate("SeriesExporter", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Export Series to CSV</span></p></body></html>", None))

