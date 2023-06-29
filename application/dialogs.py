from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox

from application import consts
from application.consts import *
from application.consts import DELAYED_SINGLE_LEAP_PATH, DECREASING_EXP_PATH
from application.consts import SINUSOID_PATH, MEANDER_PATH, SAW_PATH
from plot_modelling import PlotType


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(ABOUT_PATH, self)
        self.setWindowTitle(consts.ABOUT_US_TITLE)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.confirm.clicked.connect(self.close)


class DelayedSingleImpulse(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(DELAYED_SINGLE_IMPULSE_PATH, self)
        self.setWindowTitle(consts.DELAYED_SINGLE_IMPULSE_NAME)
        self.plot_type = PlotType.delayed_single_impulse
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(n0=int(self.n_0.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText())
                        )
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()
        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class SinusoidDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(SINUSOID_PATH, self)
        self.plot_type = PlotType.sinusoid
        self.setWindowTitle(consts.DELAYED_SINGLE_IMPULSE_NAME)
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        from utils import model_plot
        try:
            data = dict(a=int(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        fi=float(self.fi.toPlainText()),
                        w=float(self.w.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()
        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class SawDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(SAW_PATH, self)
        self.setWindowTitle(consts.SAW_NAME)
        self.plot_type = PlotType.saw
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(l=int(self.l.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()
        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class MeanderDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(MEANDER_PATH, self)
        self.setWindowTitle(consts.MEANDER_NAME)
        self.plot_type = PlotType.meander
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(l=int(self.l.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()
        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class DelayedSingleLeap(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(DELAYED_SINGLE_LEAP_PATH, self)
        self.setWindowTitle(consts.DELAYED_SINGLE_LEAP_NAME)
        self.plot_type = PlotType.delayed_single_leap
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(n0=int(self.n_0.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()
        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class DecreasingExp(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(DECREASING_EXP_PATH, self)
        self.setWindowTitle(consts.DECREASING_EXP_NAME)
        self.plot_type = PlotType.decreasing_exp
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()
        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class ExpEnvelope(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(EXP_ENVELOPE_PATH, self)
        self.setWindowTitle(consts.EXP_ENVELOPE_NAME)
        self.plot_type = PlotType.exp_envelope
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        t=float(self.t.toPlainText()),
                        fn=float(self.fn.toPlainText()),
                        fi=float(self.fi.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()

        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class BalanceEnvelope(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(BALANCE_ENVELOPE_PATH, self)
        self.setWindowTitle(consts.BALANCE_ENVELOPE_NAME)
        self.plot_type = PlotType.balance_envelope
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        fo=float(self.fo.toPlainText()),
                        fn=float(self.fn.toPlainText()),
                        fi=float(self.fi.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()

        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class TonalEnvelope(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(TONAL_ENVELOPE_PATH, self)
        self.setWindowTitle(consts.TONAL_ENVELOPE_NAME)
        self.plot_type = PlotType.tonal_envelope
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        fo=float(self.fo.toPlainText()),
                        fn=float(self.fn.toPlainText()),
                        fi=float(self.fi.toPlainText()),
                        m=float(self.m.toPlainText()))
            model_plot(self.parent(), plot_type=self.plot_type, **data)
            self.close()

        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


class LinearFrequencyModulation(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(LINEAR_FREQUENCY_MODULATION_PATH, self)
        self.setWindowTitle(consts.LINEAR_FREQUENCY_MODULATION_NAME)
        self.plot_type = PlotType.linear_frequency_modulation
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        fo=float(self.fo.toPlainText()),
                        fk=float(self.fk.toPlainText()),
                        fi=float(self.fi.toPlainText()))

        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')
        model_plot(self.parent(), plot_type=self.plot_type, **data)


class WhiteNoiseDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(WHITE_NOISE_INTERVAL_PATH, self)
        self.setWindowTitle(consts.WHITE_NOISE_INTERVAL_NAME)
        self.plot_type = PlotType.white_noise
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        b=float(self.b.toPlainText()))

        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')
        model_plot(self.parent(), plot_type=self.plot_type, **data)


class WhiteNoiseNormalisedDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(WHITE_NOISE_NORMAL_LAW_PATH, self)
        self.setWindowTitle(consts.WHITE_NOISE_NORMAL_LAW_NAME)
        self.plot_type = PlotType.white_noise_normalised
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
        self.build_plot_button.clicked.connect(self.btn_clicked)
        if self.parent().signal.frequency:
            self.frequency_text_edit.setPlainText(str(self.parent().signal.frequency))

    def btn_clicked(self):
        data = {}
        from utils import model_plot
        try:
            data = dict(a=float(self.a.toPlainText()),
                        frequency=float(self.frequency_text_edit.toPlainText()),
                        sigma=float(self.sigma.toPlainText()))

        except ValueError:
            open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')
        model_plot(self.parent(), plot_type=self.plot_type, **data)


class FragmentDialog(QDialog):
    def __init__(self, plot_widget=None):
        super(QDialog, self).__init__()
        uic.loadUi(FRAGMENT_PATH, self)
        self.plot_widget = plot_widget

        self.setupUi()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())
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


class BaseOperationDialog(QDialog):
    def __init__(self, parent=None, operation=None, operation_sign=''):
        super(QDialog, self).__init__(parent=parent)
        uic.loadUi(OPERATION_PATH, self)
        self.names = list(self.parent().signal.plots.keys())
        self.operation = operation
        self.operation_sign = operation_sign
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(self.width(), self.height())

        if self.operation_sign == '+':
            self.setWindowTitle('Сложение каналов')
        elif self.operation_sign == '*':
            self.setWindowTitle('Умножение каналов')

        self.operand_1.addItems(self.names)
        self.operand_2.addItems(self.names)
        self.calculate_button.clicked.connect(self.clicked)
        self.show()

    def clicked(self):
        from utils import add_data_to_plots
        name_1 = self.operand_1.currentText()
        name_2 = self.operand_2.currentText()
        data = {f'{name_1} {self.operation_sign} {name_2}':
                    self.operation(self.parent().signal.plots[name_1],
                                   self.parent().signal.plots[name_2])}
        self.parent().signal.plots |= data
        if name_1 and name_2:
            add_data_to_plots(
                self.parent(),
                data)
        else:
            open_warning_messagebox('Ошибка!', 'Не выбраны все операнды!')


class AdditionDialog(BaseOperationDialog):
    def __init__(self, parent=None):
        from utils import sum_plots
        super().__init__(parent=parent, operation=sum_plots, operation_sign='+')


class MultiplicationDialog(BaseOperationDialog):
    def __init__(self, parent=None):
        from utils import multiple_plots
        super().__init__(parent=parent, operation=multiple_plots, operation_sign='*')


def open_warning_messagebox(title, text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setText(text)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.buttonClicked.connect(msg_box.close)
    return_value = msg_box.exec()
