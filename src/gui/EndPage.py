import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QBrush, QColor
from PyQt5.QtWidgets import QGraphicsScene


class EndPage(object):
    def __init__(self, window):
        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(7)
        self.label = QtWidgets.QLabel(window)
        self.tab1Widget = QtWidgets.QTabWidget(window)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_3 = QtWidgets.QWidget()
        self.tab = QtWidgets.QWidget()
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_3)
        self.label_10 = QtWidgets.QLabel(self.tab_3)

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab_2)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.setup_ui(window)

    def setup_ui(self, form):
        form.setObjectName("form")
        form.setWindowModality(QtCore.Qt.ApplicationModal)
        form.resize(1250, 900)
        form.setMinimumSize(QtCore.QSize(1250, 900))
        form.setMaximumSize(QtCore.QSize(1250, 900))
        form.setFont(self.main_font)
        self.tab1Widget.setGeometry(QtCore.QRect(10, 40, 1220, 860))
        self.tab1Widget.setObjectName("tab1Widget")
        self.tab.setObjectName("tab")
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 1200, 830))
        self.graphicsView.setObjectName("graphicsView")
        self.label_2.setGeometry(QtCore.QRect(100, 10, 400, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tab1Widget.addTab(self.tab, "")
        self.tab_2.setObjectName("tab_2")
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 40, 1200, 830))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_3.setGeometry(QtCore.QRect(100, 10, 400, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tab1Widget.addTab(self.tab_2, "")

        self.graphicsView_3.setGeometry(QtCore.QRect(10, 40, 1200, 830))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label_10.setGeometry(QtCore.QRect(100, 10, 400, 21))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_3")
        self.tab1Widget.addTab(self.tab_3, "")

        self.label.setGeometry(QtCore.QRect(20, 10, 500, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslate_ui(form)
        self.tab1Widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("window", "Projek_OE_wyniki"))
        self.label_2.setText(_translate("window", "Wartości funkcji od kolejnej iteracji"))
        self.tab1Widget.setTabText(self.tab1Widget.indexOf(self.tab), _translate("form", "Wykres 1"))
        self.label_3.setText(_translate("window", "Średniej wartości funkcji"))
        self.label_10.setText(_translate("window", "Odchylenia standardowego od kolejnej iteracji"))
        self.tab1Widget.setTabText(self.tab1Widget.indexOf(self.tab_2), _translate("form", "Wykres 2"))
        self.tab1Widget.setTabText(self.tab1Widget.indexOf(self.tab_3), _translate("form", "Wykres 3"))
        self.label.setText(_translate("window", "Czas wykonywania: XXX"))

    def set_time(self, time):
        time_text = "Czas wykonywania: " + str(time) + "sec"
        self.label.setText(time_text)

    def set_fist_graph(self, name):
        path_img = '../plots/' + name
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(path_img).scaled(1200, 800))
        self.graphicsView.setScene(scene)

    def set_second_graph(self, name):
        path_img = '../plots/' + name
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(path_img).scaled(1200, 800))
        self.graphicsView_2.setScene(scene)

    def set_third_graph(self, name):
        path_img = '../plots/' + name
        scene = QGraphicsScene()
        scene.addPixmap(QPixmap(path_img).scaled(1200, 800))
        self.graphicsView_3.setScene(scene)

