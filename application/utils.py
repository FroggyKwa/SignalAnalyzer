import os

from PyQt5.QtWidgets import QFileDialog, QCheckBox

import plot_modelling
from dialogs import AboutDialog, DelayedSingleImpulse, DelayedSingleLeap, DecreasingExp, BalanceEnvelope, TonalEnvelope, \
    LinearFrequencyModulation
from dialogs import ExpEnvelope
from dialogs import FragmentDialog, SawDialog, SinusoidDialog, MeanderDialog, WhiteNoiseDialog, \
    WhiteNoiseNormalisedDialog
from dialogs import open_warning_messagebox
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


def save_file_dialog(mainwindow):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    filename, _ = QFileDialog.getSaveFileName(mainwindow,
                                              caption="Сохранить файл",
                                              filter="Text files (*.txt);;All Files (*)",
                                              directory=os.getcwd(),
                                              options=options)
    if filename:
        return filename


def add_data_to_plots(window, plots, **kwargs):
    from plot_widget import MyPlotWidget
    n = len(window.plots) + len(plots)
    for name, plot in plots.items():
        window.plots.append(
            MyPlotWidget(
                window,
                plot_data=plot,
                frequency=kwargs.get('frequency') or window.signal.frequency))
        window.graphs_layout.addWidget(window.plots[-1])
        checkbox = MyCheckBox(name, window.plots[-1], checked=True)
        checkbox.stateChanged.connect(checkbox.change_visible)
        window.name_plot_layout.addWidget(checkbox)
        window.plots[-1].plot(*plot, pen='b')
        window.plots[-1].setMouseEnabled(x=True, y=False)
        window.plots[-1].setLabel(axis='bottom', text=name)

        for p in window.plots:
            p.setFixedSize(window.size().width() - 50, (window.size().height() - 70) // n - 10)


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


def open_delayed_single_impulse_dialog(parent=None):
    DelayedSingleImpulse(parent=parent).exec()


def open_delayed_single_leap_dialog(parent=None):
    DelayedSingleLeap(parent=parent).exec()


def open_decreasing_exp_dialog(parent=None):
    DecreasingExp(parent=parent).exec()


def open_white_noise_dialog(parent=None):
    WhiteNoiseDialog(parent=parent).exec()


def open_white_noise_normalised_dialog(parent=None):
    WhiteNoiseNormalisedDialog(parent=parent).exec()


def model_plot(window, plot_type=None, **kwargs):
    try:
        duration = window.signal.duration if window.signal.duration is not None else 60
        data = {plot_modelling.generate_name(window.signal, plot_type.name): plot_modelling.model_plot(
            plot_type=plot_type, duration=duration, **kwargs)}
        window.signal.plots |= data
        add_data_to_plots(
            window,
            data,
            frequency=kwargs.get('frequency'))
    except ValueError:
        open_warning_messagebox('Ошибка!', 'Неверный формат ввода!')


def open_sinusoid_dialog(parent=None):
    SinusoidDialog(parent=parent).exec()


def open_exp_envelope_dialog(parent=None):
    ExpEnvelope(parent=parent).exec()


def open_balance_envelope_dialog(parent=None):
    BalanceEnvelope(parent=parent).exec()


def open_tonal_envelope_dialog(parent=None):
    TonalEnvelope(parent=parent).exec()


def linear_frequency_modulation_dialog(parent=None):
    LinearFrequencyModulation(parent=parent).exec()


def open_saw_dialog(parent=None):
    SawDialog(parent).exec()


def open_meander_dialog(parent=None):
    MeanderDialog(parent=parent).exec()


def sum_plots(p1, p2):
    return p1[0], [p1[1][i] + p2[1][i] for i in range(len(p1[1]))]


def multiple_plots(p1, p2):
    return p1[0], [p1[1][i] * p2[1][i] for i in range(len(p1[1]))]


def save_as(filename, signal):
    header = list()
    try:
        header.append('# channels number')
        header.append(len(signal.plots))
        header.append('# samples number')
        header.append(signal.n_signals)
        header.append('# sampling rate')
        header.append(signal.frequency)
        header.append('# start date')
        header.append(signal.start_datetime.strftime("%d-%m-%Y"))
        header.append('# start time')
        header.append(signal.start_datetime.strftime("%H:%M:%S.%f"))
        header.append('# channels names')
        header.append(';'.join(list(signal.plots.keys())))
        header = map(str, header)
        data = [[] for _ in range(signal.n_signals)]
        for i in range(signal.n_signals):
            for j in range(len(signal.plots)):
                data[i].append(list(signal.plots.values())[j][1][i])
            # data[i % len(data)].append(values[i])
    except AttributeError:
        open_warning_messagebox('Ошибка!', 'Что-то пошло не так при сохранении!')
        return

    with open(filename, 'w') as file:
        file.writelines(map(lambda x: x + '\n', header))
        for line in data:
            file.writelines(map(lambda x: x + ' ', map(str, line)))
            file.write('\n')
