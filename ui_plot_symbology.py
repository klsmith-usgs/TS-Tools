# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lcmap\TSTools-master\tstools\ui\ui_plot_symbology.ui'
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

class Ui_Plot_Symbology(object):
    def setupUi(self, Plot_Symbology):
        Plot_Symbology.setObjectName(_fromUtf8("Plot_Symbology"))
        Plot_Symbology.resize(596, 322)
        self.gridLayout = QtGui.QGridLayout(Plot_Symbology)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_box = QtGui.QDialogButtonBox(Plot_Symbology)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_box.sizePolicy().hasHeightForWidth())
        self.button_box.setSizePolicy(sizePolicy)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 1, 0, 1, 2)
        self.widget_2 = QtGui.QWidget(Plot_Symbology)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.stack_metadata = QtGui.QStackedWidget(self.widget_2)
        self.stack_metadata.setObjectName(_fromUtf8("stack_metadata"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stack_metadata.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stack_metadata.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stack_metadata, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget = QtGui.QWidget(Plot_Symbology)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 2)
        self.stack_band = QtGui.QStackedWidget(self.widget)
        self.stack_band.setObjectName(_fromUtf8("stack_band"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.stack_band.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.stack_band.addWidget(self.page_4)
        self.gridLayout_3.addWidget(self.stack_band, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 2)
        self.combox_series = QtGui.QComboBox(self.widget)
        self.combox_series.setObjectName(_fromUtf8("combox_series"))
        self.gridLayout_3.addWidget(self.combox_series, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Plot_Symbology)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), Plot_Symbology.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), Plot_Symbology.reject)
        QtCore.QMetaObject.connectSlotsByName(Plot_Symbology)

    def retranslateUi(self, Plot_Symbology):
        Plot_Symbology.setWindowTitle(_translate("Plot_Symbology", "Plot Symbology", None))
        self.label.setText(_translate("Plot_Symbology", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Metadata</span></p></body></html>", None))
        self.label_3.setText(_translate("Plot_Symbology", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Band</span></p></body></html>", None))
        self.label_2.setText(_translate("Plot_Symbology", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Series</span></p></body></html>", None))

