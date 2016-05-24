# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lcmap\TSTools-master\tstools\ui\ui_attach_md.ui'
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

class Ui_AttachMd(object):
    def setupUi(self, AttachMd):
        AttachMd.setObjectName(_fromUtf8("AttachMd"))
        AttachMd.resize(480, 480)
        self.gridLayout = QtGui.QGridLayout(AttachMd)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_box = QtGui.QDialogButtonBox(AttachMd)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 1)
        self.widget = QtGui.QWidget(AttachMd)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.widget_4 = QtGui.QWidget(self.widget)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 75))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.rad_date = QtGui.QRadioButton(self.widget_4)
        self.rad_date.setEnabled(False)
        self.rad_date.setObjectName(_fromUtf8("rad_date"))
        self.gridLayout_4.addWidget(self.rad_date, 1, 1, 1, 1)
        self.rad_ID = QtGui.QRadioButton(self.widget_4)
        self.rad_ID.setEnabled(False)
        self.rad_ID.setObjectName(_fromUtf8("rad_ID"))
        self.gridLayout_4.addWidget(self.rad_ID, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.widget_4, 2, 0, 1, 1)
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.table_metadata = QtGui.QTableWidget(self.widget_3)
        self.table_metadata.setObjectName(_fromUtf8("table_metadata"))
        self.table_metadata.setColumnCount(0)
        self.table_metadata.setRowCount(0)
        self.gridLayout_5.addWidget(self.table_metadata, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget_3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.but_add_metadata = QtGui.QPushButton(self.widget_3)
        self.but_add_metadata.setObjectName(_fromUtf8("but_add_metadata"))
        self.gridLayout_5.addWidget(self.but_add_metadata, 2, 0, 1, 1)
        self.label_5.raise_()
        self.table_metadata.raise_()
        self.but_add_metadata.raise_()
        self.gridLayout_3.addWidget(self.widget_3, 4, 0, 1, 1)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.edit_delim = QtGui.QLineEdit(self.widget_2)
        self.edit_delim.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_delim.setObjectName(_fromUtf8("edit_delim"))
        self.gridLayout_2.addWidget(self.edit_delim, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.cbox_header = QtGui.QCheckBox(self.widget_2)
        self.cbox_header.setChecked(True)
        self.cbox_header.setObjectName(_fromUtf8("cbox_header"))
        self.gridLayout_2.addWidget(self.cbox_header, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_metadata = QtGui.QLineEdit(self.widget_2)
        self.edit_metadata.setObjectName(_fromUtf8("edit_metadata"))
        self.gridLayout_2.addWidget(self.edit_metadata, 1, 1, 1, 2)
        self.but_load = QtGui.QPushButton(self.widget_2)
        self.but_load.setObjectName(_fromUtf8("but_load"))
        self.gridLayout_2.addWidget(self.but_load, 2, 3, 1, 1)
        self.but_browse = QtGui.QPushButton(self.widget_2)
        self.but_browse.setObjectName(_fromUtf8("but_browse"))
        self.gridLayout_2.addWidget(self.but_browse, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.widget_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(AttachMd)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), AttachMd.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), AttachMd.reject)
        QtCore.QMetaObject.connectSlotsByName(AttachMd)

    def retranslateUi(self, AttachMd):
        AttachMd.setWindowTitle(_translate("AttachMd", "Plot Symbology - Attach Metadata", None))
        self.rad_date.setText(_translate("AttachMd", "Date", None))
        self.rad_ID.setText(_translate("AttachMd", "ID", None))
        self.label_4.setText(_translate("AttachMd", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Match Attribute:</span></p></body></html>", None))
        self.label_5.setText(_translate("AttachMd", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Select Match Column:</span></p></body></html>", None))
        self.but_add_metadata.setText(_translate("AttachMd", "Add Metadata", None))
        self.edit_delim.setText(_translate("AttachMd", ",", None))
        self.label_3.setText(_translate("AttachMd", "Delimeter", None))
        self.cbox_header.setText(_translate("AttachMd", "Header", None))
        self.label_2.setText(_translate("AttachMd", "File", None))
        self.but_load.setText(_translate("AttachMd", "Load", None))
        self.but_browse.setText(_translate("AttachMd", "Browse", None))
        self.label.setText(_translate("AttachMd", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Open Metadata</span></p></body></html>", None))

