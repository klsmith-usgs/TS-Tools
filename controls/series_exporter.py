""" Time series export to CSV dialog
"""
import csv
import itertools
import logging
import os

import numpy as np
from PyQt4 import QtCore, QtGui

from .. import settings
from ..logger import qgis_log
from ..ui_series_exporter import Ui_SeriesExporter
from ..ui_series_exporter_item import Ui_SeriesExporterItem


def series_to_csv(fname, series,
                  date_format='%Y-%m-%d', fmt='%10.5f',
                  **kwargs):
    with open(fname, 'w') as fid:
        writer = csv.writer(fid)
        header = ['Date'] + series.band_names
        writer.writerow(header)
        for d, obs in itertools.izip(series.images['date'], series.data.T):
            row = [d.strftime(date_format)] + [fmt % o for o in obs]
            writer.writerow(row)


class SeriesExporterItem(QtGui.QWidget, Ui_SeriesExporterItem):
    def __init__(self, idx, series):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        out_name = '{desc}.csv'.format(
            desc=series.description.replace(' ', '_'))

        self.idx = idx
        self.series = series
        self.path = os.path.join(os.getcwd(), out_name)

        # Series index
        self.lab_series.setText('<b>Series {}:</b>'.format(idx))
        # Toggle writing
        self.enabled = True
        self.cbox_enable.setChecked(self.enabled)
        self.cbox_enable.stateChanged.connect(self._toggle_enable)
        # Label
        self.cbox_enable.setText('"{}"'.format(series.description))
        # Path editor
        self.edit_path.setText(self.path)
        self.edit_path.editingFinished.connect(self._edited_path)
        # Browse button
        self.but_browse.clicked.connect(self._filebrowser)

    @QtCore.pyqtSlot()
    def _filebrowser(self):
        # Get directory to open for file browser
        dirpath = str(self.edit_path.text())
        dirpath = (os.path.dirname(dirpath) if os.path.exists(dirpath)
                   else os.getcwd())

        # Open dialog
        path = self._format_path(str(QtGui.QFileDialog.getSaveFileName(
            self,
            'Select a destination for output CSV file',
            dirpath,
            'Comma-Separated Value (*.csv)'
        )))
        # Assign if passes test
        if self._test_path(path):
            self.path = path
            self.edit_path.setText(path)

    @QtCore.pyqtSlot()
    def _edited_path(self):
        path = self._format_path(str(self.edit_path.text()))
        if self._test_path(path):
            self.path = path

    @QtCore.pyqtSlot(int)
    def _toggle_enable(self, state):
        self.enabled = True if state == QtCore.Qt.Checked else False
        self.edit_path.setEnabled(self.enabled)
        self.but_browse.setEnabled(self.enabled)

    def _test_path(self, path):
        path_dirname = os.path.dirname(path)
        if (os.path.exists(path) and os.access(path, os.W_OK) or
                not os.path.exists(path) and os.access(path_dirname, os.W_OK)):
            return True
        else:
            qgis_log("Cannot write output CSV to: {}".format(path),
                     level=logging.WARNING)
            return False

    def _format_path(self, path):
        return os.path.abspath(os.path.expanduser(path))


class SeriesExporter(QtGui.QDialog, Ui_SeriesExporter):
    """ Export series within a timeseries driver

    Args:
        driver (AbstractTimeSeriesDriver): an implementation of
            ``AbstractTimeSeriesDriver`` containing one or more ``Series``
    """
    def __init__(self, driver):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.driver = driver
        self.n_series = len(self.driver.series)
        self.series_items = []
        for idx, series in enumerate(self.driver.series):
            _item = SeriesExporterItem(idx, series)
            self.scroll_area.widget().layout().addWidget(_item)
            self.series_items.append(_item)

        # Add expander to fill GUI
        self.spacer = QtGui.QSpacerItem(20, 40,
                                        QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Expanding)
        self.scroll_area.widget().layout().addItem(self.spacer)

        # Add and wire "Export" button
        self.export = QtGui.QPushButton('Export')
        self.export.setDefault(True)
        self.button_box.addButton(self.export,
                                  QtGui.QDialogButtonBox.ApplyRole)

        self.export.clicked.connect(self._export_series)

    def _export_series(self):
        success = True
        for series, series_item in zip(self.driver.series, self.series_items):
            if not series_item.enabled:
                continue
            try:
                series_to_csv(series_item.path, series, **settings.savetxt)
            except Exception as e:
                msg = ('Could not export series "{desc}" to {fname}: {err}'
                       .format(desc=series.description,
                               fname=series_item.path,
                               err=str(e)))
                qgis_log(msg, level=logging.WARNING)
                success = False
            else:
                msg = ('Exported series "{desc}" to CSV {fname}'
                       .format(desc=series.description,
                               fname=series_item.path))
                qgis_log(msg, level=logging.INFO)

        if success:
            self.close()

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    class Series(object):
        description = 'A series'

    class Driver(object):
        description = 'A driver'

    driver = Driver()
    driver.series = []
    for i in range(5):
        _series = Series()
        _series.data = np.random.rand(4, 100)
        driver.series.append(_series)

    window = SeriesExporter(driver)
    window.show()
    sys.exit(app.exec_())
