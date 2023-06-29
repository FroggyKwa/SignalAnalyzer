from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox

from application import consts
from application.consts import ABOUT_PATH, FRAGMENT_PATH, SINUSOID_PATH, MEANDER_PATH, SAW_PATH
from application.consts import ABOUT_PATH, FRAGMENT_PATH, DELAYED_SINGLE_IMPULSE


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(ABOUT_PATH, self)
        self.setWindowTitle(consts.ABOUT_US_TITLE)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.confirm.clicked.connect(self.close)



class SinusoidDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(SINUSOID_PATH, self)
        self.setWindowTitle(consts.SINUSOID_NAME)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.pushButton.clicked.connect(self.close)


class SawDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(SAW_PATH, self)
        self.setWindowTitle(consts.SAW_NAME)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.pushButton.clicked.connect(self.close)


class MeanderDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(MEANDER_PATH, self)
        self.setWindowTitle(consts.MEANDER_NAME)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.pushButton.clicked.connect(self.close)

class FragmentDialog(QDialog):
    def __init__(self, plot_widget=None):
        super(QDialog, self).__init__()
        uic.loadUi(FRAGMENT_PATH, self)
        self.plot_widget = plot_widget

        self.setupUi()

    def setupUi(self):
        self.ok_button.clicked.connect(self.ok_button_handler)

        self.end_button.clicked.connect(self.end_button_handler)

    def ok_button_handler(self):
        try:
            border_left = float(self.start.toPlainText())
            border_right = float(self.stop.toPlainText())
        except TypeError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')
        self.plot_widget.open_scaled_plot(border_left=border_left,
                                          border_right=border_right)
        self.close()

    def end_button_handler(self):
        self.stop.setPlainText(str(self.plot_widget.plot_data[0][-1]))



class DelayedSingleImpulse(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        uic.loadUi(DELAYED_SINGLE_IMPULSE, self)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(349, 190)
        self.build_plot_button.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        pass


def open_warning_messagebox(title, text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.buttonClicked.connect(msg_box.close)
    return_value = msg_box.exec()
