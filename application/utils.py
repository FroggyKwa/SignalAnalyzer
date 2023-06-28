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
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.buttonClicked.connect(msg_box.close)
    return_value = msg_box.exec()
