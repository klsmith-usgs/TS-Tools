# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\lcmap\TSTools-master\tstools\ui\ui_plotsave.ui'
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

class Ui_PlotSave(object):
    def setupUi(self, PlotSave):
        PlotSave.setObjectName(_fromUtf8("PlotSave"))
        PlotSave.resize(360, 360)
        self.gridLayout = QtGui.QGridLayout(PlotSave)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget_2 = QtGui.QWidget(PlotSave)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.edit_plot_fname = QtGui.QLineEdit(self.widget_2)
        self.edit_plot_fname.setObjectName(_fromUtf8("edit_plot_fname"))
        self.horizontalLayout_2.addWidget(self.edit_plot_fname)
        self.but_plot_fname = QtGui.QPushButton(self.widget_2)
        self.but_plot_fname.setMaximumSize(QtCore.QSize(85, 16777215))
        self.but_plot_fname.setObjectName(_fromUtf8("but_plot_fname"))
        self.horizontalLayout_2.addWidget(self.but_plot_fname)
        self.gridLayout.addWidget(self.widget_2, 4, 0, 1, 2)
        self.label_3 = QtGui.QLabel(PlotSave)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.line = QtGui.QFrame(PlotSave)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.widget = QtGui.QWidget(PlotSave)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.combox_plot_format = QtGui.QComboBox(self.widget)
        self.combox_plot_format.setObjectName(_fromUtf8("combox_plot_format"))
        self.combox_plot_format.addItem(_fromUtf8(""))
        self.combox_plot_format.addItem(_fromUtf8(""))
        self.combox_plot_format.addItem(_fromUtf8(""))
        self.combox_plot_format.addItem(_fromUtf8(""))
        self.combox_plot_format.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.combox_plot_format)
        self.lab_plot_format = QtGui.QLabel(self.widget)
        self.lab_plot_format.setMaximumSize(QtCore.QSize(85, 16777215))
        self.lab_plot_format.setObjectName(_fromUtf8("lab_plot_format"))
        self.horizontalLayout_3.addWidget(self.lab_plot_format)
        self.gridLayout.addWidget(self.widget, 5, 0, 1, 2)
        self.label = QtGui.QLabel(PlotSave)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtGui.QWidget(PlotSave)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.formLayout = QtGui.QFormLayout(self.widget_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lab_facecolor = QtGui.QLabel(self.widget_3)
        self.lab_facecolor.setObjectName(_fromUtf8("lab_facecolor"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lab_facecolor)
        self.edit_facecolor = QtGui.QLineEdit(self.widget_3)
        self.edit_facecolor.setObjectName(_fromUtf8("edit_facecolor"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.edit_facecolor)
        self.lab_edgecolor = QtGui.QLabel(self.widget_3)
        self.lab_edgecolor.setObjectName(_fromUtf8("lab_edgecolor"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.lab_edgecolor)
        self.edit_edgecolor = QtGui.QLineEdit(self.widget_3)
        self.edit_edgecolor.setObjectName(_fromUtf8("edit_edgecolor"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.edit_edgecolor)
        self.lab_transparent = QtGui.QLabel(self.widget_3)
        self.lab_transparent.setObjectName(_fromUtf8("lab_transparent"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lab_transparent)
        self.cbox_transparent = QtGui.QCheckBox(self.widget_3)
        self.cbox_transparent.setObjectName(_fromUtf8("cbox_transparent"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cbox_transparent)
        self.gridLayout.addWidget(self.widget_3, 7, 0, 1, 2)
        self.lab_plot_fname = QtGui.QLabel(PlotSave)
        self.lab_plot_fname.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lab_plot_fname.setObjectName(_fromUtf8("lab_plot_fname"))
        self.gridLayout.addWidget(self.lab_plot_fname, 2, 0, 1, 1)
        self.bbox_choice = QtGui.QDialogButtonBox(PlotSave)
        self.bbox_choice.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Save)
        self.bbox_choice.setObjectName(_fromUtf8("bbox_choice"))
        self.gridLayout.addWidget(self.bbox_choice, 8, 0, 1, 1)

        self.retranslateUi(PlotSave)
        QtCore.QMetaObject.connectSlotsByName(PlotSave)

    def retranslateUi(self, PlotSave):
        PlotSave.setWindowTitle(_translate("PlotSave", "Export Plot", None))
        self.but_plot_fname.setText(_translate("PlotSave", "Open", None))
        self.label_3.setText(_translate("PlotSave", "Matplotlib options:", None))
        self.combox_plot_format.setItemText(0, _translate("PlotSave", "png", None))
        self.combox_plot_format.setItemText(1, _translate("PlotSave", "pdf", None))
        self.combox_plot_format.setItemText(2, _translate("PlotSave", "ps", None))
        self.combox_plot_format.setItemText(3, _translate("PlotSave", "eps", None))
        self.combox_plot_format.setItemText(4, _translate("PlotSave", "svg", None))
        self.lab_plot_format.setText(_translate("PlotSave", "Format", None))
        self.label.setText(_translate("PlotSave", "<html><head/><body><p><span style=\" font-weight:600;\">Save Plot</span></p></body></html>", None))
        self.lab_facecolor.setText(_translate("PlotSave", "facecolor", None))
        self.lab_edgecolor.setText(_translate("PlotSave", "edgecolor", None))
        self.lab_transparent.setText(_translate("PlotSave", "transparent", None))
        self.cbox_transparent.setText(_translate("PlotSave", "Turn on/off transparency", None))
        self.lab_plot_fname.setText(_translate("PlotSave", "Output location:", None))

