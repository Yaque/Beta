from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from queue import Queue

from voice_capture_thread import VoiceCaptureThread
from voice_save_thread import VoiceSaveThread
from bai_du_api_thread import BaiDuAPIThread

class LineShow(object):
    """
    UI配置
    """
    queue_frames = Queue(10)
    queue_name = Queue(10)

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.WindowModal)

        # main_window.setWindowIcon(QIcon('images/logo.png'))

        self.line_show = main_window

        # 获取屏幕宽高
        self.desktop = QDesktopWidget()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        main_window.move(int(self.width / 4), self.height - 220)
        main_window.resize(int(self.width / 2), 200)
        # main_window.setWindowFlags(Qt.WindowStaysOnTopHint)
        main_window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        main_window.setAttribute(Qt.WA_TranslucentBackground)

        self.main_window = main_window

        self.centralWidget = QtWidgets.QWidget(main_window)
        self.centralWidget.setObjectName("centralWidget")


        self.btn_stop = QtWidgets.QPushButton(self.centralWidget)
        self.btn_stop.setGeometry(QtCore.QRect(0, 80, 40, 40))
        self.btn_stop.setStyleSheet("QPushButton{border-image: url(images/btn_stop0.png)}"
                                     "QPushButton:hover{border-image: url(images/btn_stop.png)}")

        self.work_thread = BaiDuAPIThread(123, "bai_du_api_thread", self.queue_name)
        self.work_thread.signOut.connect(self.slot_reshow)

        self.slot_start()

        self.ts_label0 = QtWidgets.QLabel(self.centralWidget)
        self.ts_label0.setGeometry(QtCore.QRect(50, 10, 220, 60))
        self.ts_label0.setText("12:12:12 >> 12:12:24")
        self.ts_label0.setFont(QFont("Timers", 16))
        self.ts_label0.setObjectName("ts_label0")

        self.label0 = QtWidgets.QLabel(self.centralWidget)
        self.label0.setGeometry(QtCore.QRect(275, 10, int(int(self.width / 2) - self.width / 4), 60))
        self.label0.setText("请稍后")
        self.label0.setFont(QFont("Timers", 24))
        self.label0.setObjectName("label0")
        # self.label0.setFrameShape(QtWidgets.QFrame.Box)

        self.ts_label1 = QtWidgets.QLabel(self.centralWidget)
        self.ts_label1.setGeometry(QtCore.QRect(50, 70, 220, 60))
        self.ts_label1.setText("12:12:12 >> 12:12:24")
        self.ts_label1.setFont(QFont("Timers", 16))
        self.ts_label1.setObjectName("ts_label1")

        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(275, 70, int(int(self.width / 2) - self.width / 4), 60))
        self.label1.setText("请稍后")
        self.label1.setFont(QFont("Timers", 24))
        self.label1.setObjectName("label1")
        # self.label1.setFrameShape(QtWidgets.QFrame.Box)

        # 时间显示框
        self.ts_label2 = QtWidgets.QLabel(self.centralWidget)
        self.ts_label2.setGeometry(QtCore.QRect(50, 130, 220, 60))
        self.ts_label2.setText("12:12:12 >> 12:12:24")
        self.ts_label2.setFont(QFont("Timers", 16))
        self.ts_label2.setObjectName("ts_label2")

        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(275, 130, int(int(self.width / 2) - self.width / 4), 60))
        self.label2.setText("请稍后")
        self.label2.setFont(QFont("Timers", 24))
        self.label2.setObjectName("label2")
        # self.label2.setFrameShape(QtWidgets.QFrame.Box)

        # main_window.setCentralWidget(self.centralWidget)
        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # 开始按钮按下后使其不可用，启动线程
    def slot_start(self):
        self.work_thread.start()
        self.save_thread = VoiceSaveThread(1234, "save_thread", self.queue_frames, self.queue_name)
        self.save_thread.start()

        self.voice_thread = VoiceCaptureThread(12, "capture_thread", self.queue_frames, self.queue_name)
        self.voice_thread.start()

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_stop.clicked.connect(self.back_main)

    def back_main(self):
        self.work_thread.signOut.disconnect(self.slot_reshow)
        self.work_thread.stop()
        self.work_thread.exit()

        self.voice_thread.stop()
        self.save_thread.stop()

        self.voice_thread.join(0.1)
        self.save_thread.join(0.1)

        self.line_show.close()
        # self.main_window.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

    def slot_reshow(self, data):
        data = data.split("+:+")
        if data[1] == '0':
            self.ts_label0.setText(data[0])
            self.label0.setText(data[2])
        elif data[1] == '1':
            self.ts_label1.setText(data[0])
            self.label1.setText(data[2])
        elif data[1] == '2':
            self.ts_label2.setText(data[0])
            self.label2.setText(data[2])


