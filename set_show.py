from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from sqlite_util import query, update


class SetShow(object):

    def setup_ui(self, SET):
        SET.setObjectName("SET")
        SET.resize(360, 210)
        SET.setWindowIcon(QIcon('images/logo.png'))
        SET.setStyleSheet("border-image:url(images/main_bk.png)")
        self.set=SET

        self.btn_back = QtWidgets.QPushButton(SET)
        self.btn_back.setGeometry(QtCore.QRect(190, 140, 100, 60))
        self.btn_back.setObjectName("btn_back")

        self.edit_app_id = QtWidgets.QLineEdit(self.set)
        self.edit_app_id.setGeometry(QtCore.QRect(100, 40, 250, 20))
        self.edit_app_id.setObjectName("edit_app_id")

        self.edit_api_key = QtWidgets.QLineEdit(self.set)
        self.edit_api_key.setGeometry(QtCore.QRect(100, 70, 250, 20))
        self.edit_api_key.setText("")
        self.edit_api_key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_api_key.setObjectName("edit_api_key")

        self.edit_secret_key = QtWidgets.QLineEdit(self.set)
        self.edit_secret_key.setGeometry(QtCore.QRect(100, 100, 250, 20))
        self.edit_secret_key.setText("")
        self.edit_secret_key.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edit_secret_key.setObjectName("edit_secret_key")

        self.label_app_id = QtWidgets.QLabel(self.set)
        self.label_app_id.setGeometry(QtCore.QRect(10, 40, 60, 20))
        self.label_app_id.setTextFormat(QtCore.Qt.AutoText)
        self.label_app_id.setObjectName("label_app_id")

        self.label_api_key = QtWidgets.QLabel(self.set)
        self.label_api_key.setGeometry(QtCore.QRect(10, 70, 60, 20))
        self.label_api_key.setObjectName("label_api_key")

        self.label_secret_key = QtWidgets.QLabel(self.set)
        self.label_secret_key.setGeometry(QtCore.QRect(10, 100, 60, 20))
        self.label_secret_key.setObjectName("label_secret_key")

        self.label_info = QtWidgets.QLabel(self.set)
        self.label_info.setGeometry(QtCore.QRect(120, 10, 120, 20))
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setObjectName("label_info")

        self.btn_update = QtWidgets.QPushButton(self.set)
        self.btn_update.setGeometry(QtCore.QRect(70, 140, 100, 60))
        self.btn_update.setObjectName("btn_update")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(SET)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.set.setWindowTitle(_translate("SET", "设置"))
        self.btn_back.setText(_translate("SET", "返回"))
        self.btn_back.clicked.connect(self.back_main)

        self.edit_app_id.setPlaceholderText(_translate("SET", "请输入APP_ID"))
        self.edit_api_key.setPlaceholderText(_translate("SET", "请输入API_KEY"))
        self.edit_secret_key.setPlaceholderText(_translate("SET", "请输入SECRET_KEY"))
        self.get_set()

        self.label_app_id.setText(_translate("SET", "APP_ID"))
        self.label_api_key.setText(_translate("SET", "API_KEY"))
        self.label_secret_key.setText(_translate("SET", "SECRET_KEY"))
        self.label_info.setText(_translate("SET", "欢迎进入设置页面"))

        self.btn_update.setText(_translate("SET", "更新"))
        self.btn_update.clicked.connect(self.update_set)

    def get_set(self):
        datas = query()
        self.edit_app_id.setText(datas[1])
        self.edit_api_key.setText(datas[2])
        self.edit_secret_key.setText(datas[3])

    def update_set(self):
        app_id = self.edit_app_id.text()
        api_key = self.edit_api_key.text()
        secret_key = self.edit_secret_key.text()
        if app_id == '' or api_key == '' or secret_key == '':
            self.label_info.setText("信息错误")
            self.edit_app_id.setFocus()
        else:
            self.label_info.setText("设置成功")
            update(app_id, api_key, secret_key)


    def back_main(self):
        self.set.close()