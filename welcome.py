from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie, QIcon



class WelcomeShow(object):
    def setup_ui(self, Welcome, UiMain):
        Welcome.setObjectName("Welcome")

        Welcome.setWindowIcon(QIcon('images/logo.png'))
        self.welcome = Welcome
        self.window_s_ui = UiMain
        Welcome.setWindowFlags(Qt.FramelessWindowHint)
        Welcome.setWindowModality(QtCore.Qt.WindowModal)
        Welcome.resize(360, 270)

        self.timer = QTimer()  # 初始化一个定时器
        self.timer.timeout.connect(self.operate_wait)  # 计时结束调用operate()方法
        self.timer.start(5500)  # 设置计时间隔并启动

        self.label_welcome_gif = QtWidgets.QLabel(Welcome)
        self.label_welcome_gif.setGeometry(QtCore.QRect(0, 0, 360, 270))
        self.label_welcome_gif.setObjectName("label_welcome_gif")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.welcome.setWindowTitle(_translate("Welcome", "welcome"))
        self.set_gif()

    def set_gif(self):
        self.welcome_gif = QMovie('images/welcome.gif')
        self.label_welcome_gif.setMovie(self.welcome_gif)
        self.welcome_gif.start()

    def operate_wait(self):
        window_main = QtWidgets.QWidget()
        self.window_s_ui.setup_ui(window_main)
        window_main.show()
        self.timer.stop()
        self.welcome.close()

if __name__ == "__main__":
    pass
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # welcome_show = QtWidgets.QWidget()
    # welcome_s_ui = WelcomeShow()
    # window_s_ui = UiMain()
    #
    # welcome_s_ui.setup_ui(welcome_show)
    # welcome_show.show()
    # sys.exit(app.exec_())