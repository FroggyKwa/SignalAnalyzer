import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox

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


def open_warning_messagebox(title, text):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText(text)
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.buttonClicked.connect(msgBox.close)
    returnValue = msgBox.exec()
