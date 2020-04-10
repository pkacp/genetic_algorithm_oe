# import sys
# import time
#
# from PyQt5 import QtCore, QtGui, QtWidgets
#
# from src.BinaryChromosome import BinaryChromosome
# from src.DataAnalyzer import DataAnalyzer
# from src.Evolution import Evolution
# from src.Functions import Functions
# from src.enums.CrossingType import CrossingType
# from src.enums.MutationType import MutationType
# from src.enums.SelectionType import SelectionType
# from src.gui.EndPage import EndPage
#
#
# class MainPage(object):
#     def __init__(self, window):
#         self.second_window = QtWidgets.QMainWindow()
#         self.main_font = QtGui.QFont()
#         self.main_font.setPointSize(7)
#
#         self.PrecisionSpinBox = QtWidgets.QSpinBox(window)
#         self.PopulationSpinBox = QtWidgets.QSpinBox(window)
#         self.EraSpinBox = QtWidgets.QSpinBox(window)
#         self.SelectionMethodComboBox = QtWidgets.QComboBox(window)
#         self.SelectionSpinBox = QtWidgets.QSpinBox(window)
#         self.CrossComboBox = QtWidgets.QComboBox(window)
#         self.CrossDoubleSpinBox = QtWidgets.QDoubleSpinBox(window)
#         self.MutationComboBox = QtWidgets.QComboBox(window)
#         self.MutationDoubleSpinBox = QtWidgets.QDoubleSpinBox(window)
#         self.InversionCheckBox = CheckBox(window)
#         self.InversionDoubleSpinBox = QtWidgets.QDoubleSpinBox(window)
#         self.EliteCheckBox = CheckBox(window)
#         self.EliteSpinBox = QtWidgets.QSpinBox(window)
#         self.x1FromSpinBox = QtWidgets.QSpinBox(window)
#         self.x1ToSpinBox = QtWidgets.QSpinBox(window)
#         # self.x2FromSpinBox = QtWidgets.QSpinBox(window)
#         # self.x2ToSpinBox = QtWidgets.QSpinBox(window)
#         self.StartButton = QtWidgets.QPushButton(window)
#         self.label_13 = QtWidgets.QLabel(window)
#         self.label_12 = QtWidgets.QLabel(window)
#         # self.label_11 = QtWidgets.QLabel(window)
#         # self.label_10 = QtWidgets.QLabel(window)
#         self.label_9 = QtWidgets.QLabel(window)
#         self.label_8 = QtWidgets.QLabel(window)
#         self.label_7 = QtWidgets.QLabel(window)
#         self.label_6 = QtWidgets.QLabel(window)
#         self.label_5 = QtWidgets.QLabel(window)
#         self.label_4 = QtWidgets.QLabel(window)
#         self.label_3 = QtWidgets.QLabel(window)
#         self.label_2 = QtWidgets.QLabel(window)
#         self.label = QtWidgets.QLabel(window)
#
#     def setup_ui(self, window):
#
#         window.setObjectName("Dialog")
#         window.setWindowModality(QtCore.Qt.ApplicationModal)
#         window.setEnabled(True)
#         window.resize(420, 500)
#         window.setFont(self.main_font)
#         window.setMinimumSize(QtCore.QSize(420, 500))
#         window.setMaximumSize(QtCore.QSize(420, 500))
#         window.setWindowTitle("Projekt_1_OE - Kacprzak, Łyś")
#         # Dialog.setSizeGripEnabled(False)
#         keyPressed = QtCore.pyqtSignal(QtCore.QEvent)
#
#         self.StartButton.setGeometry(QtCore.QRect(150, 450, 93, 28))
#         self.StartButton.setDefault(True)
#         self.StartButton.setObjectName("StartButton")
#         self.StartButton.clicked.connect(lambda: self.start())
#
#         self.EraSpinBox.setGeometry(QtCore.QRect(110, 130, 91, 22))
#         self.EraSpinBox.setToolTipDuration(-3)
#         self.EraSpinBox.setMinimum(1)
#         self.EraSpinBox.setObjectName("EraSpinBox")
#
#         self.PopulationSpinBox.setGeometry(QtCore.QRect(110, 90, 91, 22))
#         self.PopulationSpinBox.setToolTipDuration(-3)
#         self.PopulationSpinBox.setMinimum(1)
#         self.PopulationSpinBox.setMaximum(10000)
#         self.PopulationSpinBox.setObjectName("PopulationSpinBox")
#         self.PopulationSpinBox.valueChanged.connect(lambda: self.after_population_change())
#
#         self.PrecisionSpinBox.setGeometry(QtCore.QRect(110, 50, 91, 22))
#         self.PrecisionSpinBox.setToolTipDuration(-3)
#         self.PrecisionSpinBox.setMinimum(1)
#         self.PrecisionSpinBox.setObjectName("PrecisionSpinBox")
#
#         self.label.setGeometry(QtCore.QRect(20, 50, 71, 21))
#         self.label.setObjectName("label")
#
#         self.label_2.setGeometry(QtCore.QRect(20, 90, 71, 21))
#         self.label_2.setObjectName("label_2")
#
#         self.label_3.setGeometry(QtCore.QRect(20, 130, 71, 21))
#         self.label_3.setObjectName("label_3")
#
#         self.SelectionMethodComboBox.setGeometry(QtCore.QRect(110, 170, 91, 21))
#         self.SelectionMethodComboBox.setObjectName("SelectionMethodComboBox")
#         self.SelectionMethodComboBox.addItems(["Najlepszych", "Ruletki", "Truniejowej"])
#
#         self.label_4.setGeometry(QtCore.QRect(20, 170, 91, 21))
#         self.label_4.setObjectName("label_4")
#
#         self.label_5.setGeometry(QtCore.QRect(20, 210, 91, 21))
#         self.label_5.setObjectName("label_5")
#
#         self.CrossComboBox.setGeometry(QtCore.QRect(110, 210, 91, 21))
#         self.CrossComboBox.setObjectName("CrossComboBox")
#         self.CrossComboBox.addItems(["Jedno punkt.", "Dwu punkt.", "Trzy punkt."])
#
#         self.label_6.setGeometry(QtCore.QRect(20, 250, 91, 21))
#         self.label_6.setObjectName("label_6")
#
#         self.MutationComboBox.setGeometry(QtCore.QRect(110, 250, 91, 21))
#         self.MutationComboBox.setObjectName("MutationComboBox")
#         self.MutationComboBox.addItems(["Jedno punkt.", "Dwu punkt.", "Brzegowa"])
#
#         self.EliteSpinBox.setGeometry(QtCore.QRect(110, 330, 91, 22))
#         self.EliteSpinBox.setToolTipDuration(-3)
#         self.EliteSpinBox.setMinimum(0)
#         self.EliteSpinBox.setObjectName("EliteSpinBox")
#
#         self.label_7.setGeometry(QtCore.QRect(20, 330, 91, 21))
#         self.label_7.setObjectName("label_7")
#
#         self.x1FromSpinBox.setGeometry(QtCore.QRect(110, 370, 51, 22))
#         self.x1FromSpinBox.setToolTipDuration(-3)
#         self.x1FromSpinBox.setMinimum(-99)
#         self.x1FromSpinBox.setObjectName("x1FromSpinBox")
#         self.x1FromSpinBox.valueChanged.connect(lambda: self.update_minimum_x1())
#
#         self.label_8.setGeometry(QtCore.QRect(20, 370, 71, 21))
#         self.label_8.setObjectName("label_8")
#
#         self.label_9.setGeometry(QtCore.QRect(170, 370, 21, 21))
#         self.label_9.setObjectName("label_9")
#
#         self.x1ToSpinBox.setGeometry(QtCore.QRect(190, 370, 51, 22))
#         self.x1ToSpinBox.setToolTipDuration(-3)
#         self.x1ToSpinBox.setMinimum(self.x1FromSpinBox.value()+1)
#         self.x1ToSpinBox.setObjectName("x1ToSpinBox_3")
#
#         # self.x2ToSpinBox.setGeometry(QtCore.QRect(190, 400, 51, 22))
#         # self.x2ToSpinBox.setToolTipDuration(-3)
#         # self.x2ToSpinBox.setMinimum(self.x2FromSpinBox.value())
#         # self.x2ToSpinBox.setObjectName("x2ToSpinBox_4")
#         #
#         # self.x2FromSpinBox.setGeometry(QtCore.QRect(110, 400, 51, 22))
#         # self.x2FromSpinBox.setToolTipDuration(-3)
#         # self.x2FromSpinBox.setMinimum(-99)
#         # self.x2FromSpinBox.setObjectName("x2FromSpinBox_5")
#         # self.x2FromSpinBox.valueChanged.connect(lambda: self.update_minimum_x2())
#
#         # self.label_10.setGeometry(QtCore.QRect(170, 400, 21, 21))
#         # self.label_10.setObjectName("label_10")
#         # self.label_11.setGeometry(QtCore.QRect(20, 400, 71, 21))
#         # self.label_11.setObjectName("label_11")
#
#         self.label_12.setGeometry(QtCore.QRect(20, 290, 91, 21))
#         self.label_12.setObjectName("label_12")
#
#         self.InversionDoubleSpinBox.setGeometry(QtCore.QRect(110, 290, 91, 22))
#         self.InversionDoubleSpinBox.setToolTipDuration(-3)
#         self.InversionDoubleSpinBox.setMinimum(0)
#         self.InversionDoubleSpinBox.setObjectName("InwersionSpinBox_3")
#         self.InversionDoubleSpinBox.setMaximum(1.0)
#         self.InversionDoubleSpinBox.setSingleStep(0.01)
#
#         self.InversionCheckBox.setGeometry(QtCore.QRect(210, 290, 170, 20))
#         self.InversionCheckBox.setObjectName("InversionCheckBox")
#         self.InversionCheckBox.clicked.connect(lambda: self.change_inversion())
#
#         self.EliteCheckBox.setGeometry(QtCore.QRect(210, 330, 160, 20))
#         self.EliteCheckBox.setObjectName("EliteCheckBox")
#         self.EliteCheckBox.clicked.connect(lambda: self.change_elite())
#
#         self.label_13.setGeometry(QtCore.QRect(16, 10, 341, 31))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setItalic(False)
#         font.setWeight(75)
#         self.label_13.setFont(font)
#         self.label_13.setObjectName("label_13")
#
#         self.SelectionSpinBox.setGeometry(QtCore.QRect(220, 170, 62, 22))
#         self.SelectionSpinBox.setObjectName("SelectionDoubleSpinBox")
#         self.SelectionSpinBox.setMaximum(self.PopulationSpinBox.value())
#
#         self.CrossDoubleSpinBox.setGeometry(QtCore.QRect(220, 210, 62, 22))
#         self.CrossDoubleSpinBox.setObjectName("CrossDoubleSpinBox")
#         self.CrossDoubleSpinBox.setMaximum(1.0)
#         self.CrossDoubleSpinBox.setSingleStep(0.01)
#
#         self.MutationDoubleSpinBox.setGeometry(QtCore.QRect(220, 250, 62, 22))
#         self.MutationDoubleSpinBox.setObjectName("MutationDoubleSpinBox")
#         self.MutationDoubleSpinBox.setMaximum(1.0)
#         self.MutationDoubleSpinBox.setSingleStep(0.01)
#
#         self.retranslate_ui(window)
#         QtCore.QMetaObject.connectSlotsByName(window)
#
#     def retranslate_ui(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         self.StartButton.setText(_translate("Dialog", "Start"))
#         self.label.setText(_translate("Dialog", "Dokładność"))
#         self.label_2.setText(_translate("Dialog", "Populacja"))
#         self.label_3.setText(_translate("Dialog", "Liczba epok"))
#         self.label_4.setText(_translate("Dialog", "Metoda selekcji"))
#         self.label_5.setText(_translate("Dialog", "Krzyżowanie"))
#         self.label_6.setText(_translate("Dialog", "Mutacja"))
#         self.label_7.setText(_translate("Dialog", "Strat. Elitarnej"))
#         self.label_8.setText(_translate("Dialog", "Zakres x od"))
#         self.label_9.setText(_translate("Dialog", "do"))
#         # self.label_10.setText(_translate("Dialog", "do"))
#         # self.label_11.setText(_translate("Dialog", "Zakres x2 od"))
#         self.label_12.setText(_translate("Dialog", "Inwesja"))
#         self.InversionCheckBox.setText(_translate("Dialog", "Aktualnie: Z inwesją"))
#         self.EliteCheckBox.setText(_translate("Dialog", "Aktualnie: Procentowo"))
#         self.label_13.setText(_translate("Dialog", "Optymalizacja - Funkcja Levyego"))
#
#     def change_inversion(self):
#         if self.InversionCheckBox.isChecked():
#             self.InversionDoubleSpinBox.setDisabled(True)
#             self.InversionDoubleSpinBox.setValue(0)
#             self.InversionCheckBox.setText("Aktualnie: Bez inwesji")
#         else:
#             self.InversionDoubleSpinBox.setDisabled(False)
#             self.InversionCheckBox.setText("Aktualnie: Z inwesją")
#
#     def change_elite(self):
#         if self.EliteCheckBox.isChecked():
#             self.EliteCheckBox.setText("Aktualnie: L. osobników")
#             self.EliteSpinBox.setValue(int((self.EliteSpinBox.value()*self.PopulationSpinBox.value())))
#             self.EliteSpinBox.setMaximum(self.PopulationSpinBox.value())
#         else:
#             self.EliteCheckBox.setText("Aktualnie: Procentowo")
#             self.EliteSpinBox.setValue(int((self.EliteSpinBox.value()/self.PopulationSpinBox.value())*100))
#             self.EliteSpinBox.setMaximum(100)
#
#     def update_minimum_x1(self):
#         self.x1ToSpinBox.setMinimum(self.x1FromSpinBox.value()+1)
#
#     # def update_minimum_x2(self):
#     #     self.x2ToSpinBox.setMinimum(self.x2FromSpinBox.value())
#
#     def update_max_selection(self):
#         self.SelectionSpinBox.setMaximum(self.PopulationSpinBox.value())
#
#     def get_elite(self):
#         if not self.EliteCheckBox.isChecked():
#             return int(self.PopulationSpinBox.value() * (self.EliteSpinBox.value() / 100))
#         else:
#             return int(self.PopulationSpinBox.value())
#
#     def get_selection_type(self):
#         actual = self.SelectionMethodComboBox.currentText()
#         if actual == "Ruletki":
#             return SelectionType.ROULETTE
#         elif actual == "Najlepszych":
#             return SelectionType.BEST
#         else:
#             return SelectionType.TOURNAMENT
#
#     def get_mutation_type(self):
#         actual = self.MutationComboBox.currentText()
#         if actual == "Jedno punkt.":
#             return MutationType.ONE_POINT
#         elif actual == "Dwu punkt.":
#             return MutationType.TWO_POINT
#         else:
#             return MutationType.THREE_POINT
#
#     def get_cross_type(self):
#         actual = self.CrossComboBox.currentText()
#         if actual == "Jedno punkt.":
#             return CrossingType.ONE_POINT
#         elif actual == "Dwu punkt.":
#             return CrossingType.TWO_POINT
#         else:
#             return CrossingType.THREE_POINT
#
#     def after_population_change(self):
#         self.update_max_selection()
#         self.change_elite()
#
#     def start(self):
#         selection_args = []
#         epochs = self.EraSpinBox.value()
#         population_size = self.PopulationSpinBox.value()
#         range_start = self.x1FromSpinBox.value()
#         range_end = self.x1ToSpinBox.value()
#         accuracy = self.PrecisionSpinBox.value()
#         function = Functions.levy_function
#         searching_value = min
#         chromosome_type = BinaryChromosome
#         number_of_chromosomes = 2
#         selection_type = self.get_selection_type()
#         selection_args.append(self.SelectionSpinBox.value())  # depending from selection type(tournament size/number
#         # of individuals to pick)
#         crossing_type = self.get_cross_type()
#         crossing_prob = self.CrossDoubleSpinBox.value()
#         mutation_type = self.get_mutation_type()
#         mutation_prob = self.MutationDoubleSpinBox.value()
#         inversion_prob = self.InversionDoubleSpinBox.value()
#         keeping_elite_num = self.get_elite()
#
#         evolution = Evolution(epochs, population_size, range_start, range_end, accuracy, function, searching_value,
#                               chromosome_type, number_of_chromosomes, selection_type, selection_args, crossing_type,
#                               crossing_prob, mutation_type, mutation_prob, inversion_prob, keeping_elite_num)
#
#         start_time = time.time()
#         evolution.run()
#
#         # parameters about plots
#         function_value_from_iteration = True
#         mean_function_value_from_iteration = True
#         sd_from_iteration = True
#
#         print("_________________________________________")
#         da = DataAnalyzer(evolution, function_value_from_iteration, mean_function_value_from_iteration,
#                           sd_from_iteration)
#         da.plotting_and_saving_to_csv()
#         pic = da.get_list()
#         finish_time = round(time.time() - start_time, 2)
#
#         gui = EndPage(self.second_window)
#         gui.set_fist_graph(pic[0])
#         gui.set_second_graph(pic[1])
#         gui.set_third_graph(pic[2])
#         gui.set_time(finish_time)
#         self.second_window.show()
#
#
# class CheckBox(QtWidgets.QCheckBox):
#     def keyPressEvent(self, event):
#         if event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
#             self.click()
#         super(CheckBox, self).keyPressEvent(event)
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = QtWidgets.QMainWindow()
#     ui = MainPage(window)
#     ui.setup_ui(window)
#     window.show()
#     sys.exit(app.exec_())
