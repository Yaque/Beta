from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtCore import Qt

import sys

from line_show import LineShow
from set_show import SetShow

from config import STREAM, P


class UiMain(object):
    def setup_ui(self, Main):
        Main.setObjectName("Main")
        Main.resize(360, 280)
        Main.setWindowIcon(QIcon('images/logo.png'))
        Main.setStyleSheet("border-image:url(images/main_bk.png)")
        self.main = Main

        self.label_gif = QtWidgets.QLabel(Main)
        self.label_gif.setGeometry(QtCore.QRect(10, 10, 340, 150))
        self.label_gif.setObjectName("label_gif")
        self.set_gif()

        self.btn_start = QtWidgets.QPushButton(Main)
        self.btn_start.setGeometry(QtCore.QRect(10, 180, 90, 90))
        self.btn_start.setObjectName("btn_start")
        self.btn_start.setAttribute(Qt.WA_TranslucentBackground)
        self.btn_start.setStyleSheet("QPushButton{border-image: url(images/btn_start_bk_0.png)}"
                                        "QPushButton:hover{border-image: url(images/btn_start_bk_1.png)}")

        self.btn_set = QtWidgets.QPushButton(Main)
        self.btn_set.setGeometry(QtCore.QRect(110, 180, 60, 60))
        self.btn_set.setObjectName("btn_set")

        self.btn_exit = QtWidgets.QPushButton(Main)
        self.btn_exit.setGeometry(QtCore.QRect(180, 180, 75, 25))
        self.btn_exit.setObjectName("btn_exit")

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.main.setWindowTitle(_translate("Main", "随堂字幕系统"))
        # self.label_gif.setText(_translate("Main", "随堂字幕"))
        self.btn_start.setText(_translate("Main", "开始"))
        self.btn_start.clicked.connect(self.activity_start)
        self.btn_set.setText(_translate("Main", "设置"))
        self.btn_set.clicked.connect(self.set_show)
        self.btn_exit.setText(_translate("Main", "退出"))

        self.btn_exit.clicked.connect(self.exit)

    def set_gif(self):
        self.r_logo_gif = QMovie("images/r_logo.gif")
        self.label_gif.setMovie(self.r_logo_gif)
        self.r_logo_gif.start()

    def activity_start(self):
        self.main.hide()
        line_s = QtWidgets.QDialog()
        l_s_ui = LineShow()
        l_s_ui.setup_ui(line_s)
        line_s.show()
        line_s.exec_()
        self.main.show()
        # self.btn_start.setStyleSheet("QPushButton:pressed{border-image: url(images/btn_start_bk_2.png)}"
        #                              "QPushButton:hover{border-image: url(images/btn_start_bk_1.png)}")

    def set_show(self):
        self.main.hide()
        set_s = QtWidgets.QDialog()
        s_s_ui = SetShow()
        s_s_ui.setup_ui(set_s)
        set_s.show()
        set_s.exec_()
        self.main.show()

    def exit(self):
        STREAM.stop_stream()
        STREAM.close()
        P.terminate()
        self.main.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t_main = QtWidgets.QWidget()
    window = UiMain()
    window.setup_ui(t_main)
    t_main.show()
    sys.exit(app.exec_())
