import os

from PyQt5.QtWidgets import QFileDialog, QCheckBox

from dialogs import FragmentDialog, AboutDialog, DelayedSingleImpulse
from dialogs import FragmentDialog, SawDialog, SinusoidDialog, MeanderDialog
from views.information_dialog import InformationDialog


def open_file_dialog(mainwindow):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getOpenFileName(mainwindow,
                                              caption="Открыть файл",
                                              filter="Text files (*.txt);;All Files (*)",
                                              directory=os.getcwd(),
                                              options=options)
    if filename:
        mainwindow.setup_signal_from_file(filename)


def show_signal_information(**info):
    info_dialog = InformationDialog(**info)
    info_dialog.exec()


def show_fragment_dialog(plot_widget):
    fragment_dialog = FragmentDialog(plot_widget)
    fragment_dialog.exec()


class MyCheckBox(QCheckBox):
    def __init__(self, name, plot, checked=True):
        super().__init__(name, checked=checked)
        self.plot = plot

    def change_visible(self):
        if self.isChecked():
            self.plot.show()
        else:
            self.plot.hide()


def open_about_us_dialog():
    AboutDialog().exec()


def open_delayed_single_impulse_dialog():
    DelayedSingleImpulse().exec()

def open_sinusoid_dialog():
    SinusoidDialog().exec()

def open_saw_dialog():
    SawDialog().exec()

def open_meander_dialog():
    MeanderDialog().exec()